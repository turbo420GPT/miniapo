import streamlit as st
import requests  # Для отправки сообщений в Telegram
import sqlite3

API_TOKEN = '7936064458:AAF9nK8kQ-anW1wUCzqJrb69ePjGI7UVPXk'
BASE_URL = f'https://api.telegram.org/bot{API_TOKEN}'

def get_user_balance(username):
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM users WHERE username = ?', (username,))
balance = cursor.fetchone()
    conn.close()
    return balance[0] if balance else 0

def send_click(username):
    requests.get(f'{BASE_URL}/sendMessage?chat_id={username}&text=/click')

def get_top_users():
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username, balance FROM users ORDER BY balance DESC LIMIT 10')
    users = cursor.fetchall()
    conn.close()
    return users

# Основная логика приложения Streamlit
st.title("Кликер Telegram")

username = st.text_input("Введите ваше имя пользователя (username):")

if username:
    balance = get_user_balance(username)
    st.write(f"**Ваш баланс:** {balance}")

    if st.button("Клик", key='click_button'):
        send_click(username)
        st.success("Клик отправлен! Проверьте ваш Telegram.")

    st.sidebar.title("Топ игроков")
    top_users = get_top_users()
    for rank, (user, user_balance) in enumerate(top_users, 1):
        st.sidebar.write(f"{rank}. {user} - {user_balance}")

