import sqlite3
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (id INT, username TEXT, password TEXT)')
cursor.execute("INSERT INTO users VALUES (1, 'admin', 'supersecret')")
cursor.execute("INSERT INTO users VALUES (2, 'alice', 'alice123')")
conn.commit()

def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("Query:", query)
    cursor.execute(query)
    return cursor.fetchone()

print("Attacker Login:", login("' OR '1'='1' --", "anything"))
