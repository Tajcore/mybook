import mysql.connector
from faker import Faker
from mysql.connector import Error
from werkzeug.security import generate_password_hash
from datetime import datetime
import random
random_names = Faker() 
date = datetime.now()
domains = ["cheerful","wink","snakes","overjoyed","tasty","pricey","prick","sick","handy","books","tow","mine","whine","tooth","obeisant","stupendous","flame","zebra","powder","program","locket","eggs","ask","reproduce","hug","cave","exciting","humor","provide","meal","secretive","underwear","comparison","grape","few","tired","roll","greet","addition","preach","exercise","minor","surprise","fold","meat","coach","tight","damage","curly","small","excellent","gold","winter","show","oranges","women","tongue","settle","kneel","nosy","cheap","steep","hammer","flagrant","bore","abortive","base","boorish","care","jumpy","loose","amazing","wrench","lunch","fall","amusement","courageous","substantial","daily","kindhearted","questionable","chivalrous","helpful","tendency","porter","magic","foamy","test","plants","deliver","statement","cause","flash","plough","shame","scintillating","obnoxious","button","nail","quirky"]
connection = mysql.connector.connect(host='localhost',
                                         database='mybook',
                                         user='root',
                                         password='password',
                                         auth_plugin='mysql_native_password')
if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT e_mail from USER")
        rs = cursor.fetchall()
        emails = [email[0] for email in rs]
        file_ = open("new_setup_db3.sql","a")
        for _ in range(100000):
                name = random_names.name().split(" ")
                first_name_1 = name[0]
                last_name_1 = name[1]
                email_1 = first_name_1 + last_name_1 + "@" +random.choice(domains) +".com"
                while email_1 in emails:
                        email_1 = first_name_1 + last_name_1 + "@" +random.choice(domains) +".com"
                password_1 = "password123"
                password_1 = generate_password_hash(password_1, method='pbkdf2:sha256')
                query_user = "INSERT INTO USER(f_name,l_name,e_mail,password,date_created) VALUES('{}','{}','{}','{}','{}');\n".format(first_name_1,last_name_1,email_1,password_1,date)
                query_profile = "INSERT INTO PROFILE(user_id,profile_pic,dob,biography,gender,location) VALUES(LAST_INSERT_ID(),'user.png','1000-01-01','none','none','none');\n"
                file_.write(query_user)
                file_.write(query_profile)
                emails.append(email_1)
        print("500000 Users Added")
        file_.close()





