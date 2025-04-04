import sqlite3

def init_db():
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    
    # Создание таблицы пользователей, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            balance INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username):
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (username) VALUES (?)', (username,))
    conn.commit()
    conn.close()

def update_balance(username, amount):
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET balance = balance + ? WHERE username = ?', (amount, username))
    conn.commit()
    conn.close()

def get_top_users(limit=15):
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username, balance FROM users ORDER BY balance DESC LIMIT ?', (limit,))
    top_users = cursor.fetchall()
    conn.close()
    return top_users

def get_balance(username):
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM users WHERE username = ?', (username,))
    balance = cursor.fetchone()
    conn.close()
    return balance[0] if balance else 0
