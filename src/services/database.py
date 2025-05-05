import sqlite3

def get_db_connection():
    return sqlite3.connect('users.db')

def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                 )''')
    c.execute('''CREATE TABLE IF NOT EXISTS devices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    ip TEXT NOT NULL,
                    status BOOLEAN NOT NULL
                 )''')
    conn.commit()
    conn.close()

def get_user(email):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = c.fetchone()
    conn.close()
    if user:
        return {'id': user[0], 'name': user[1], 'email': user[2], 'password': user[3]}
    return None

def add_user(name, email, password):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
    conn.commit()
    conn.close()

# Initialize database on import
init_db()