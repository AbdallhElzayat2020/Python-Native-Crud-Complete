# db.py
import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # حط الباسورد بتاع MySQL هنا
        database="crud_python"
    )
