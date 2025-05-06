#!/usr/bin/env python3

import cgi
import db

print("Content-type: text/html\n")

form = cgi.FieldStorage()
user_id = form.getvalue("id")

if user_id:
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()

# رجوع للصفحة الرئيسية
print("""
    <script>
        window.location.href = '/cgi-bin/index.py';
    </script>
""")
