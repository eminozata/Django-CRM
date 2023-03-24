import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password1234",
    
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE crm")

print("Database created successfully")
