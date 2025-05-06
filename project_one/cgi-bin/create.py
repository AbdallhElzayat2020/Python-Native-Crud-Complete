# create.py
import cgi
import db

form = cgi.FieldStorage()
name = form.getvalue("name")
email = form.getvalue("email")

conn = db.connect()
cursor = conn.cursor()

cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
conn.commit()

print("Content-type: text/html\n")
print("<h3>User added successfully. <a href='/cgi-bin/index.py'>Go back</a></h3>")
