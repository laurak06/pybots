# insert
# select
import sqlite3


def insert_data(telegram_id, date):
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute("INSERT OR IGNOR INTO users (telegram_id, date_add) VALUES (?, ?)", (telegram_id, date))
    conn.commit()
    conn.close()


def select_data():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute(f"""SELECT * FROM users""")
    data = cursor.fetchall()
    conn.close()
    return data


