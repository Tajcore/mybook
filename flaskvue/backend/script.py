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
        for _ in range(10):
                name = random_names.name().split(" ")
                first_name = name[0]
                last_name = name[1]
                email = first_name + last_name + "@fakemail.com"
                password = "password123"
                password_ = generate_password_hash(password, method='pbkdf2:sha256')
                sql = "INSERT INTO User (f_name, l_name, e_mail, password, date_created) VALUES (%s, %s , %s , %s , %s)"
                val = (first_name,last_name,email,password_,date)
                cursor.execute(sql, val)
                connection.commit()
                print("1 record inserted, ID:", cursor.lastrowid)



