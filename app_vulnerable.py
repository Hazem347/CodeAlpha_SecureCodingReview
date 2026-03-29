import sqlite3

# Connect to database (it will create one if not exists)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table (only first time)
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
conn.commit()

# Insert a default user (only if not already exists)
cursor.execute("SELECT * FROM users WHERE username = 'admin'")
if not cursor.fetchone():
    cursor.execute("INSERT INTO users VALUES ('admin', '1234')")
    conn.commit()

print("=== Vulnerable Login System ===")

username = input("Enter username: ")
password = input("Enter password: ")

# ❌ VULNERABLE QUERY (SQL Injection possible)
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

print("\n[DEBUG] Executing Query:")
print(query)

cursor.execute(query)
result = cursor.fetchone()

if result:
    print("✅ Login Successful!")
else:
    print("❌ Login Failed!")

conn.close()