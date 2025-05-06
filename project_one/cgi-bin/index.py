#!/usr/bin/env python3

import db
print("Content-type: text/html\n")

print("""
<!DOCTYPE html>
<html>
  <head>
    <title>CRUD Users</title>
    <link rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  </head>
  <body class="container mt-5">

    <h2 class="mb-4">Add New User</h2>
    <form action="/cgi-bin/create.py" method="post" class="mb-5">
      <div class="mb-3">
        <input type="text" name="name" placeholder="Name" class="form-control" required />
      </div>
      <div class="mb-3">
        <input type="email" name="email" placeholder="Email" class="form-control" required />
      </div>
      <input type="submit" value="Add User" class="btn btn-primary" />
    </form>

    <h2 class="mb-3">Users List</h2>
    <table class="table table-bordered table-striped">
      <thead class="table-dark">
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Email</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
""")

conn = db.connect()
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(f"""
        <tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>
                <form action="/cgi-bin/delete.py" method="post" style="display:inline;">
                    <input type="hidden" name="id" value="{row[0]}">
                    <button type="submit" class="btn btn-danger btn-sm"
                        onclick="return confirm('Are you sure you want to delete this user?');">
                        Delete
                    </button>
                </form>
            </td>
        </tr>
    """)

print("""
      </tbody>
    </table>
  </body>
</html>
""")
