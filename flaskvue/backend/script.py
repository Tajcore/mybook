import mysql.connector
from faker import Faker
from mysql.connector import Error
from werkzeug.security import generate_password_hash
from datetime import datetime
random_names = Faker() 
date = datetime.now()
connection = mysql.connector.connect(host='localhost',
                                         database='mybook',
                                         user='root',
                                         password='password',
                                         auth_plugin='mysql_native_password')
if connection.is_connected():
        cursor = connection.cursor()
        for _ in range(50000):
                cursor.execute("SELECT e_mail from USER")
                rs = cursor.fetchall()
                emails = [email[0] for email in rs]
                name = random_names.name().split(" ")
                first_name_1 = name[0]
                last_name_1 = name[1]
                email_1 = first_name_1 + last_name_1 + "@fakemail.com"
                while email_1 in emails:
                        name = random_names.name().split(" ")
                        first_name_1 = name[0]
                        last_name_1 = name[1]
                        email_1 = first_name_1 + last_name_1 + "@fakemail.com"
                password_1 = "password123"
                password_1 = generate_password_hash(password_1, method='pbkdf2:sha256')
                name = random_names.name().split(" ")
                first_name_2 = name[0]
                last_name_2 = name[1]
                email_2 = first_name_2 + last_name_2 + "@fakemail.com"
                while email_2 in emails:
                        name = random_names.name().split(" ")
                        first_name_2 = name[0]
                        last_name_2 = name[1]
                        email_2 = first_name_2 + last_name_2 + "@fakemail.com"
                password_2 = "password123"
                password_2 = generate_password_hash(password_2, method='pbkdf2:sha256')
                name = random_names.name().split(" ")
                first_name_3 = name[0]
                last_name_3 = name[1]
                email_3 = first_name_3 + last_name_3 + "@fakemail.com"
                while email_3 in emails:
                        name = random_names.name().split(" ")
                        first_name_3 = name[0]
                        last_name_3 = name[1]
                        email_3 = first_name_3+ last_name_3 + "@fakemail.com"
                password_3 = "password123"
                password_3 = generate_password_hash(password_3, method='pbkdf2:sha256')
                name = random_names.name().split(" ")
                first_name_4 = name[0]
                last_name_4 = name[1]
                email_4 = first_name_4 + last_name_4 + "@fakemail.com"
                while email_4 in emails:
                        name = random_names.name().split(" ")
                        first_name_4 = name[0]
                        last_name_4 = name[1]
                        email_4 = first_name_4 + last_name_4 + "@fakemail.com"
                password_4 = "password123"
                password_4 = generate_password_hash(password_4, method='pbkdf2:sha256')
                name = random_names.name().split(" ")
                first_name_5 = name[0]
                last_name_5 = name[1]
                email_5 = first_name_5 + last_name_5 + "@fakemail.com"
                while email_5 in emails:
                        name = random_names.name().split(" ")
                        first_name_5 = name[0]
                        last_name_5 = name[1]
                        email_5 = first_name_5 + last_name_5 + "@fakemail.com"
                password_5 = "password123"
                password_5 = generate_password_hash(password_5, method='pbkdf2:sha256')
                name = random_names.name().split(" ")
                first_name_6 = name[0]
                last_name_6 = name[1]
                email_6 = first_name_6 + last_name_6 + "@fakemail.com"
                while email_6 in emails:
                        name = random_names.name().split(" ")
                        first_name_6 = name[0]
                        last_name_6 = name[1]
                        email_6 = first_name_6 + last_name_6 + "@fakemail.com"
                password_6 = "password123"
                password_6 = generate_password_hash(password_6, method='pbkdf2:sha256')
                name = random_names.name().split(" ")
                first_name_7 = name[0]
                last_name_7 = name[1]
                email_7 = first_name_7 + last_name_7 + "@fakemail.com"
                while email_7 in emails:
                        name = random_names.name().split(" ")
                        first_name_7 = name[0]
                        last_name_7 = name[1]
                        email_7 = first_name_7 + last_name_7 + "@fakemail.com"
                password_7 = "password123"
                password_7 = generate_password_hash(password_7, method='pbkdf2:sha256')
                name = random_names.name().split(" ")
                first_name_8 = name[0]
                last_name_8 = name[1]
                email_8 = first_name_8 + last_name_8 + "@fakemail.com"
                while email_8 in emails:
                        name = random_names.name().split(" ")
                        first_name_8 = name[0]
                        last_name_8 = name[1]
                        email_8 = first_name_8 + last_name_8 + "@fakemail.com"
                password_8 = "password123"
                password_8 = generate_password_hash(password_8, method='pbkdf2:sha256')
                name = random_names.name().split(" ")
                first_name_9 = name[0]
                last_name_9 = name[1]
                email_9 = first_name_9 + last_name_9 + "@fakemail.com"
                while email_9 in emails:
                        name = random_names.name().split(" ")
                        first_name_9 = name[0]
                        last_name_9 = name[1]
                        email_9 = first_name_9 + last_name_9 + "@fakemail.com"
                password_9 = "password123"
                password_9 = generate_password_hash(password_9, method='pbkdf2:sha256')
                name = random_names.name().split(" ")
                first_name_0 = name[0]
                last_name_0 = name[1]
                email_0 = first_name_0 + last_name_0 + "@fakemail.com"
                while email_0 in emails:
                        name = random_names.name().split(" ")
                        first_name_0 = name[0]
                        last_name_0 = name[1]
                        email_0 = first_name_0 + last_name_0 + "@fakemail.com"
                password_0 = "password123"
                password_0 = generate_password_hash(password_0, method='pbkdf2:sha256')


                sql = "INSERT INTO User (f_name, l_name, e_mail, password, date_created) VALUES (%s, %s , %s , %s , %s),(%s, %s , %s , %s , %s),(%s, %s , %s , %s , %s),(%s, %s , %s , %s , %s),(%s, %s , %s , %s , %s),(%s, %s , %s , %s , %s),(%s, %s , %s , %s , %s),(%s, %s , %s , %s , %s),(%s, %s , %s , %s , %s),(%s, %s , %s , %s , %s)"
                val = (first_name_1,last_name_1,email_1,password_1,date,first_name_2,last_name_2,email_2,password_2,date,first_name_3,last_name_3,email_3,password_3,date,first_name_4,last_name_4,email_4,password_4,date,first_name_5,last_name_5,email_5,password_5,date,first_name_6,last_name_6,email_6,password_6,date,first_name_7,last_name_7,email_7,password_7,date,first_name_8,last_name_8,email_8,password_8,date,first_name_9,last_name_9,email_9,password_9,date,first_name_0,last_name_0,email_0,password_0,date)
                cursor.execute(sql, val)
                connection.commit()
                cursor.execute("SELECT * FROM User where e_mail = '" + str(email_1) + "'")
                rv = cursor.fetchone()
                sql = "INSERT INTO Profile (user_id,profile_pic,dob,biography,gender,location) VALUES (%s, %s , %s , %s , %s,%s)"
                val = (str(rv[0]),"user.png","1000-01-01","none","none","none")
                cursor.execute(sql,val)
                cursor.execute("SELECT * FROM User where e_mail = '" + str(email_2) + "'")
                rv = cursor.fetchone()
                sql = "INSERT INTO Profile (user_id,profile_pic,dob,biography,gender,location) VALUES (%s, %s , %s , %s , %s,%s)"
                val = (str(rv[0]),"user.png","1000-01-01","none","none","none")
                cursor.execute(sql,val)
                cursor.execute("SELECT * FROM User where e_mail = '" + str(email_3) + "'")
                rv = cursor.fetchone()
                sql = "INSERT INTO Profile (user_id,profile_pic,dob,biography,gender,location) VALUES (%s, %s , %s , %s , %s,%s)"
                val = (str(rv[0]),"user.png","1000-01-01","none","none","none")
                cursor.execute(sql,val)
                cursor.execute("SELECT * FROM User where e_mail = '" + str(email_4) + "'")
                rv = cursor.fetchone()
                sql = "INSERT INTO Profile (user_id,profile_pic,dob,biography,gender,location) VALUES (%s, %s , %s , %s , %s,%s)"
                val = (str(rv[0]),"user.png","1000-01-01","none","none","none")
                cursor.execute(sql,val)
                cursor.execute("SELECT * FROM User where e_mail = '" + str(email_5) + "'")
                rv = cursor.fetchone()
                sql = "INSERT INTO Profile (user_id,profile_pic,dob,biography,gender,location) VALUES (%s, %s , %s , %s , %s,%s)"
                val = (str(rv[0]),"user.png","1000-01-01","none","none","none")
                cursor.execute(sql,val)
                cursor.execute("SELECT * FROM User where e_mail = '" + str(email_6) + "'")
                rv = cursor.fetchone()
                sql = "INSERT INTO Profile (user_id,profile_pic,dob,biography,gender,location) VALUES (%s, %s , %s , %s , %s,%s)"
                val = (str(rv[0]),"user.png","1000-01-01","none","none","none")
                cursor.execute(sql,val)
                cursor.execute("SELECT * FROM User where e_mail = '" + str(email_7) + "'")
                rv = cursor.fetchone()
                sql = "INSERT INTO Profile (user_id,profile_pic,dob,biography,gender,location) VALUES (%s, %s , %s , %s , %s,%s)"
                val = (str(rv[0]),"user.png","1000-01-01","none","none","none")
                cursor.execute(sql,val)
                cursor.execute("SELECT * FROM User where e_mail = '" + str(email_8) + "'")
                rv = cursor.fetchone()
                sql = "INSERT INTO Profile (user_id,profile_pic,dob,biography,gender,location) VALUES (%s, %s , %s , %s , %s,%s)"
                val = (str(rv[0]),"user.png","1000-01-01","none","none","none")
                cursor.execute(sql,val)
                cursor.execute("SELECT * FROM User where e_mail = '" + str(email_9) + "'")
                rv = cursor.fetchone()
                sql = "INSERT INTO Profile (user_id,profile_pic,dob,biography,gender,location) VALUES (%s, %s , %s , %s , %s,%s)"
                val = (str(rv[0]),"user.png","1000-01-01","none","none","none")
                cursor.execute(sql,val)
                cursor.execute("SELECT * FROM User where e_mail = '" + str(email_0) + "'")
                rv = cursor.fetchone()
                sql = "INSERT INTO Profile (user_id,profile_pic,dob,biography,gender,location) VALUES (%s, %s , %s , %s , %s,%s)"
                val = (str(rv[0]),"user.png","1000-01-01","none","none","none")
                cursor.execute(sql,val)
                connection.commit()
                print("10 record inserted")



