import sqlite3

def get_user_data(user_input):
  conn =sqlite3.connect('user.db')
  cursor = conn.cursor()

# Vulnerable SQL Injection query via direct string concatenatenation
query = "SELECT * FROM accounts WHERE username = '" + user_input + "'"
cursor.execute(query)

return cursor.fetchall()
