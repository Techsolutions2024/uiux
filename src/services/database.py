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
    c.execute('''CREATE TABLE IF NOT EXISTS password_reset_tokens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    token TEXT NOT NULL UNIQUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(user_id) REFERENCES users(id)
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

def store_password_reset_token(user_id, token):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO password_reset_tokens (user_id, token) VALUES (?, ?)", (user_id, token))
    conn.commit()
    conn.close()

def get_user_by_reset_token(token):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''SELECT u.id, u.name, u.email, u.password FROM users u
                 JOIN password_reset_tokens t ON u.id = t.user_id
                 WHERE t.token = ?''', (token,))
    user = c.fetchone()
    conn.close()
    if user:
        return {'id': user[0], 'name': user[1], 'email': user[2], 'password': user[3]}
    return None

def update_user_password(user_id, new_password):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE users SET password = ? WHERE id = ?", (new_password, user_id))
    conn.commit()
    conn.close()

# Initialize database on import
init_db()
