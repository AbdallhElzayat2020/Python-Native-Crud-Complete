# show.py
import db

conn = db.connect()
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Content-type: text/html\n")

for row in rows:
    print(f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>")
