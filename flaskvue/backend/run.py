
from flask import Flask, jsonify, request, json,render_template
from flask_mysqldb import MySQL
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token

app = Flask(__name__, 
            static_folder = "../frontend/static",
            template_folder = "../frontend")
UPLOAD_FOLDER = '../dist/uploads'

app.config['MYSQL_USER'] = 'db_user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'mybook'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JWT_SECRET_KEY'] = 'secret'
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

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
            sql = "INSERT INTO User (f_name, l_name, email, password, date_created) VALUES (%s, %s , %s , %s , %s)"
            val = (first_name,last_name,email,password,date)
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
        
@app.route('/login', methods= ["POST","GET"])
def login():
        if request.method == 'POST' and request.get_json()['form'] == "login":
            cur = mysql.connection.cursor()
            email = request.get_json()['email']
            password = request.get_json()['password']
            result = ""
            cur.execute("SELECT * FROM User where email = '" + str(email) + "'")
            rv = cur.fetchone()

            if bcrypt.check_password_hash(rv['password'], password):
                access_token = create_access_token(
                    identity={
                        'first_name': rv['f_name'],
                        'last_name': rv['l_name'],
                        'email': rv['email'],
                        'id' : rv['id']
                    })
                responseObj = {
                    'status': 200,
                    'message': 'Successfully login',
                    'auth_token': access_token
                }
            else:
                responseObj = {
                    'status': 400,
                    'status': 'Invalid username and password'
                }

            return responseObj
        
app.run(debug=True)
