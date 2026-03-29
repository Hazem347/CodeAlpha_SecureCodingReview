import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

print("=== Secure Login System ===")

username = input("Enter username: ")
password = input("Enter password: ")

# ✅ SECURE QUERY (Prevents SQL Injection)
query = "SELECT * FROM users WHERE username = ? AND password = ?"

cursor.execute(query, (username, password))
result = cursor.fetchone()

if result:
    print("✅ Login Successful!")
else:
    print("❌ Login Failed!")

conn.close()