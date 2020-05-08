import sys 
import os
from flask import Flask, jsonify, request, json,render_template
from flask_mysqldb import MySQL
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist")
UPLOAD_FOLDER = '../frontend/static/uploads'    

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'mybook'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JWT_SECRET_KEY'] = 'secret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mysql = MySQL(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)

@app.route('/', methods= ["GET"])
def web_page():
    return render_template("index.html")

@app.route('/register', methods= ["POST"])
def register(): 
        if request.method == 'POST' and request.get_json()['form'] == "register":
            cur = mysql.connection.cursor()
            first_name = request.get_json()['fname']
            last_name = request.get_json()['lname']
            email = request.get_json()['email']
            password = bcrypt.generate_password_hash(
            request.get_json()['password']).decode('utf-8')
            date = datetime.utcnow()
            sql = "INSERT INTO User (f_name, l_name, e_mail, password, date_created) VALUES (%s, %s , %s , %s , %s)"
            val = (first_name,last_name,email,password,date)
            cur.execute(sql,val)
            mysql.connection.commit()
            cur.execute("SELECT * FROM User where e_mail = '" + str(email) + "'")
            rv = cur.fetchone()
            sql = "INSERT INTO Profile (user_id,profile_pic,dob,biography,gender,location) VALUES (%s, %s , %s , %s , %s,%s)"
            val = (rv["id"],"user.png","1000-01-01","none","none","none")
            cur.execute(sql,val)
            mysql.connection.commit()
            result = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'password': password,
                    'created': date
                }
            return jsonify({'result': result}) 
        
@app.route('/login', methods= ["POST"])
def login():
        if request.method == 'POST' and request.get_json()['form'] == "login":
            cur = mysql.connection.cursor()
            email = request.get_json()['email']
            password = request.get_json()['password']
            result = ""
            cur.execute("SELECT * FROM User where e_mail = '" + str(email) + "'")
            rv = cur.fetchone()
            cur.execute("SELECT profile_pic FROM Profile where user_id = '" + str(rv["id"]) + "'")
            prof = cur.fetchone()
            if bcrypt.check_password_hash(rv['password'], password):
                access_token = create_access_token(
                    identity={
                        'profile_pic':update_filepath(prof['profile_pic']),
                        'first_name': rv['f_name'],
                        'last_name': rv['l_name'],
                        'e_mail': rv['e_mail'],
                        'id' : rv['id']
                    })
                result = access_token
                return result
            else:
                result = {'status': 'Invalid username and password'}
                return result

@app.route('/user/posts/<user_id>', methods=['GET'])
def Posts_and_Comments(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM POST WHERE posted_by ='"+str(user_id)+"' ORDER BY date_posted DESC")
    user_posts = cur.fetchall()
    result = [{"id":post["id"],"user":post["posted_by"],"date_posted":post["date_posted"],"img_url":update_filepath(post["post_image"]),"msg":post["post_msg"]} for post in user_posts]  
    cur.execute("CALL GetFriends("+ str(user_id)+ ")")
    rs = cur.fetchall()
    friends = []
    for friend in rs:
        if str(friend["user1_id"]) != str(user_id):
            cur.execute("SELECT * FROM POST WHERE posted_by ='"+str(friend["user1_id"])+"' ORDER BY date_posted DESC")
            friend_post = cur.fetchall()
            result+= [{"id":post["id"],"user":post["posted_by"],"date_posted":post["date_posted"],"img_url":update_filepath(post["post_image"]),"msg":post["post_msg"]} for post in friend_post]
        else:
            cur.execute("SELECT * FROM POST WHERE posted_by ='"+str(friend["user2_id"])+"' ORDER BY date_posted DESC")
            friend_post = cur.fetchall()
            result+= [{"id":post["id"],"user":post["posted_by"],"date_posted":post["date_posted"],"img_url":update_filepath(post["post_image"]),"msg":post["post_msg"]} for post in friend_post]

    for user in result:
     cur.execute("CALL FindUser("+ str(user["user"])+ ")")
     rs = cur.fetchone()
     user.update({"first_name": rs["f_name"]})
     user.update({"last_name": rs["l_name"]})
     sql = "SELECT profile_pic FROM profile WHERE user_id ="+str(rs["id"])
     cur.execute(sql)
     rs = cur.fetchone()
     user.update({"prof_pic": update_filepath(rs["profile_pic"])})
    for post in result:
        cur.execute("CALL PostComments("+ str(post["id"])+ ")")
        rs = cur.fetchall()
        comments = [{"comment_id":comment["id"],"comment_text":comment["comment_text"],"posted_by":comment["posted_by"],"posted_to":comment["posted_to"],"date_commented":comment["date_commented"]} for comment in rs]
        for comment in comments:
            cur.execute("CALL FindUser("+ str(comment["posted_by"])+ ")")
            rs = cur.fetchone()
            comment.update({"first_name": rs["f_name"]})
            comment.update({"last_name": rs["l_name"]})
            cur.execute("SELECT profile_pic FROM profile WHERE user_id ="+str(rs["id"]))
            rs = cur.fetchone()
            comment.update({"prof_pic": update_filepath(rs["profile_pic"])})
        comments.sort(key = lambda x:x["date_commented"], reverse=True)
        post.update({"Comments": comments})
    result.sort(key = lambda x:x["date_posted"], reverse=True)
    return jsonify({"posts":result})
 

@app.route('/user/post', methods = ["POST"])
def post():
     if request.method == 'POST':
            if 'file' in request.files:
                file = request.files['file'] 
                filename = secure_filename(file.filename)
                fileExt = filename.split('.')[1]
                autoGenFileName = uuid.uuid4()
                newFileName = str(autoGenFileName) + '.' + fileExt
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], newFileName)    )
            else:
                newFileName = ''
            cur = mysql.connection.cursor()
            user = request.form['user']
            msg = request.form['msg']
            date = datetime.utcnow()
            sql = "INSERT INTO POST (posted_by, date_posted,post_image,post_msg) VALUES (%s, %s , %s , %s)"
            val = (user,date,newFileName,msg)
            cur.execute(sql,val)
            mysql.connection.commit()
            result = {
                    'user': user,
                    'image': newFileName,
                    'msg': msg,
                    'date': date
                }
            return jsonify({'result': result}) 

@app.route('/user/comment', methods = ["POST"])
def comment():     
    if request.method == 'POST':
            cur = mysql.connection.cursor()
            posted_by = request.form['user']
            posted_to = request.form['posted_to']
            msg = request.form['comment_txt']
            date = datetime.utcnow()
            sql = "INSERT INTO COMMENT (posted_by, posted_to, date_commented, comment_text) VALUES (%s, %s , %s , %s)"
            val = (posted_by,posted_to,date,msg)
            cur.execute(sql,val)
            mysql.connection.commit()
            result = {
                    'posted_by': posted_by,
                    'posted_to': posted_to,
                    'msg': msg,
                    'date': date
                }
            return jsonify({'result': result}) 

@app.route('/user/profile/<user_id>', methods=['GET','POST'])
def profile(user_id):
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM PROFILE WHERE user_id ='"+str(user_id)+"'")
        profile = cur.fetchone()
        profile_details = {"location_":profile["location"],"User_id":profile["user_id"],"Profile_pic":update_filepath(profile["profile_pic"]),"dob":profile["dob"],"bio":profile["biography"],"gender":profile["gender"]}
        cur.execute("SELECT * FROM USER WHERE id ='"+str(user_id)+"'")
        rs = cur.fetchone()
        profile_details.update({"email":rs["e_mail"]})
        profile_details.update({"date_created":rs["date_created"]})
        profile_details.update({"first_name":rs["f_name"]})
        profile_details.update({"last_name":rs["l_name"]})
        return jsonify({"profile_details":profile_details})
    elif request.method == "POST":
        file = request.files['profile_pic']
        filename = secure_filename(file.filename)
        fileExt = filename.split('.')[1]
        autoGenFileName = uuid.uuid4()
        newFileName = str(autoGenFileName) + '.' + fileExt
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newFileName))
        cur= mysql.connection.cursor()
        user_id = request.form['user_id']
        email = request.form['email']
        bio = request.form['bio']
        gender = request.form['gender']
        dob = request.form['dob']
        location = request.form['location']
        cur = mysql.connection.cursor()
        args = (user_id,bio,gender,newFileName,dob,location)
        cur.callproc("UpdateProfile",args)
        sql = "UPDATE user SET e_mail = %s  WHERE id = %s"
        val = (email,user_id)
        cur.execute(sql,val)
        mysql.connection.commit()
        return jsonify({"msg":"Success"})
def update_filepath(image):
    """Add complete filepath to filenames from database"""
    if image == "none":
        image = ""
    else:
        image = '/static/uploads/' + image
    return image

@app.route('/users', methods = ["GET"])
def users():
        if request.method == "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM User")
            result = cur.fetchall()
            users = [{"user_id":rs["id"], "name":rs["f_name"]+" "+rs["l_name"]+" "+str(rs["id"]),"email":rs["e_mail"],"date_created":rs["date_created"]} for rs in result]
            for user in users:
                cur.execute("SELECT * FROM PROFILE WHERE user_id ='"+str(user["user_id"])+"'")
                rs = cur.fetchone()
                user.update({"dob":rs["dob"]})
                user.update({"profile_pic":update_filepath(rs["profile_pic"])})
                user.update({"bio":rs["biography"]})
                user.update({"gender":rs["gender"]})    
                user.update({"location":rs["location"]})    
            return jsonify({"users":users})

@app.route('/users/add', methods = ["POST","GET"])
def addUser():
    if request.method == "POST":
        user_1 = request.form["user1_id"]
        user_2 = request.form["user2_id"]
        args = (str(user_1),str(user_2))
        cur = mysql.connection.cursor()
        cur.callproc("AddFriend",args)
        mysql.connection.commit()
        result = {"user_1":user_1,
        "user_2":user_2,
        "status":0}
        return jsonify(result)

@app.route('/users/status', methods = ["POST"])
def status():
    if request.method == "POST":
        user_1 = request.form['user1_id']
        user_2 = request.form['user2_id']
        cur = mysql.connection.cursor()      
        sql = "SELECT STATUS FROM RELATIONSHIP WHERE (USER1_ID = %s AND USER2_ID = %s) OR (USER1_ID = %s AND USER2_ID = %s)"
        val = (user_1,user_2,user_2,user_1)
        cur.execute(sql,val)
        rs = cur.fetchone()
        result = {"user_1": user_2,
        "user_2":user_2,
        "status": rs["STATUS"]}
        return jsonify(result)


@app.route('/users/request/<user_id>', methods=['GET'])
def friendrequests(user_id):
   if request.method == "GET":
        cur = mysql.connection.cursor()   
        args = (str(user_id))  
        cur.execute("CALL GetFriendRequest("+str(user_id)+")")
        rs = cur.fetchall()
        users = []
        for user in rs:
            cur.execute("CALL FindUser("+ str(user["user1_id"])+ ")")
            result = cur.fetchone()
            requests = {"user_id":result["id"],"first_name":result["f_name"],"last_name":result["l_name"]}
            cur.execute("SELECT profile_pic FROM profile WHERE user_id ="+str(result["id"]))
            result = cur.fetchone()
            requests.update({"profile_pic":update_filepath(result["profile_pic"])})
            users.append(requests)
        return jsonify({"requests":users})


 
@app.route('/users/accept', methods = ["POST"])
def accept():
    if request.method == "POST":
        user_1 = request.form['user1_id']
        user_2 = request.form['user2_id']
        decision = 1
        cur = mysql.connection.cursor()      
        args = (user_1,user_2,str(decision))
        cur.callproc("AcceptFriend",args)
        mysql.connection.commit()        
        result = {"user_1": user_2,
        "user_2":user_2,
        "status": decision}
        return jsonify(result)

@app.route('/users/friends/<user_id>', methods=['GET'])
def friends(user_id):
   if request.method == "GET":
        cur = mysql.connection.cursor()      
        cur.execute("CALL GetFriends("+ str(user_id)+ ")")
        rs = cur.fetchall()
        friends = []
        for friend in rs:
            if str(friend["user1_id"]) != str(user_id):
                cur.execute("CALL FindUser("+ str(friend["user1_id"])+ ")")
                result = cur.fetchone()
                requests = {"user_id":result["id"],"first_name":result["f_name"],"last_name":result["l_name"]}
                cur.execute("SELECT profile_pic FROM profile WHERE user_id ="+str(result["id"]))
                result = cur.fetchone()
                requests.update({"profile_pic":update_filepath(result["profile_pic"])})
                friends.append(requests)
            else:
                cur.execute("CALL FindUser("+ str(friend["user2_id"])+ ")")
                result = cur.fetchone()
                requests = {"user_id":result["id"],"first_name":result["f_name"],"last_name":result["l_name"]}
                cur.execute("SELECT profile_pic FROM profile WHERE user_id ="+str(result["id"]))
                result = cur.fetchone()
                requests.update({"profile_pic":update_filepath(result["profile_pic"])})
                friends.append(requests)               
        return jsonify({"friends":friends})


@app.route('/users/groups', methods=['GET','POST'])
def groups():
    if request.method == "GET":    
        cur = mysql.connection.cursor()      
        cur.execute("SELECT * FROM GROUP_")
        rs = cur.fetchall()
        result = [{"group_id":group["id"],"group_name":group["name"],"group_creator":group["created_by"]} for group in rs]
        for group in result:
            cur.execute("CALL FindUser("+ str(group["group_creator"])+ ")")
            new_rs = cur.fetchone()
            group.update({"creator_name":new_rs["f_name"]+" "+new_rs["l_name"]})
            cur.execute("CALL GetMembers("+ str(group["group_id"])+ ")")
            members = cur.fetchall()
            group.update({"members_count":len(members)})
        return jsonify({"groups":result})
    if request.method == "POST":
        creator = request.form["user_id"]
        group_name = request.form["group_name"]
        sql = "INSERT INTO GRO  UP_(created_by,name) VALUES(%s,%s)"
        val = (str(creator),group_name)
        cur = mysql.connection.cursor()      
        cur.execute(sql,val)
        mysql.connection.commit()    
        return jsonify({"message":"success"})


@app.route('/users/group/<group_id>', methods=['GET','POST'])
def group(group_id):
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM GROUP_ WHERE id ="+str(group_id))
        rs = cur.fetchone()
        group = {"group_name":rs["name"],"group_id":rs["id"],"created_by":rs["created_by"]}
        cur.execute("CALL GETMEMBERS("+str(group_id)+")")
        result = cur.fetchall()
        members = [{"member_id":rs["id"],"member_fname":rs["f_name"],"member_lname":rs["l_name"]} for rs in result]
        for member in members:
            sql = "SELECT profile_pic FROM profile WHERE user_id ="+str(member["member_id"])
            cur.execute(sql)
            rs = cur.fetchone()
            member.update({"prof_pic": update_filepath(rs["profile_pic"])})
        group.update({"members":members})
        cur.execute("CALL GETGRPPOSTS("+str(group["group_id"])+")")
        result = cur.fetchall()
        posts = [{"post_id":post["id"],"date_posted":post["date_posted"],"post_img":update_filepath(post["post_image"]),"post_msg":post["post_msg"]} for post in result]
        for post in posts:
            cur.execute("CALL PostComments("+ str(post["post_id"])+ ")")
            rs = cur.fetchall()
            comments = [{"comment_id":comment["id"],"comment_text":comment["comment_text"],"posted_by":comment["posted_by"],"posted_to":comment["posted_to"],"date_commented":comment["date_commented"]} for comment in rs]
            for comment in comments:
                cur.execute("CALL FindUser("+ str(comment["posted_by"])+ ")")
                rs = cur.fetchone()
                comment.update({"first_name": rs["f_name"]})
                comment.update({"last_name": rs["l_name"]})
                cur.execute("SELECT profile_pic FROM profile WHERE user_id ="+str(rs["id"]))
                rs = cur.fetchone()
                comment.update({"prof_pic": update_filepath(rs["profile_pic"])})
            comments.sort(key = lambda x:x["date_commented"], reverse=True)
            post.update({"Comments": comments})
        posts.sort(key = lambda x:x["date_posted"], reverse=True)
        group.update({"group_posts":posts})
        return jsonify({"group":group})
    if request.method == "POST":
        user_id = request.form["user_id"]
        cur = mysql.connection.cursor()
        sql ="CALL JOINGROUP(%s,%s)"
        val = (str(user_id),str(group_id))
        cur.execute(sql,val)
        mysql.connection.commit()
        return jsonify({"success":"successful addition"})





@app.route('/user/group/post', methods=['GET','POST'])
def group_post():
     if request.method == 'POST':
            if 'file' in request.files:
                file = request.files['file'] 
                filename = secure_filename(file.filename)
                fileExt = filename.split('.')[1]
                autoGenFileName = uuid.uuid4()
                newFileName = str(autoGenFileName) + '.' + fileExt
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], newFileName)    )
            else:
                newFileName = ''
            cur = mysql.connection.cursor()
            group_id = request.form['group_id']
            user = request.form['user']
            msg = request.form['msg']
            date = datetime.utcnow()
            sql = "INSERT INTO POST (posted_by, date_posted,post_image,post_msg) VALUES (%s, %s , %s , %s)"
            val = (user,date,newFileName,msg)
            cur.execute(sql,val)
            mysql.connection.commit()
            post_id = cur.lastrowid
            sql = "INSERT INTO GROUP_POSTS(group_id,post_id) VALUES (%s, %s)"
            val = (group_id,post_id)
            cur.execute(sql,val)
            mysql.connection.commit()
            result = {
                    'user': user,
                    'image': newFileName,
                    'msg': msg,
                    'date': date
                }
            return jsonify({'result': result}) 
app.run(debug=True)