import sqlite3


def createTable():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        telegram_id INTEGER,
                        date_add TEXT)""")
    conn.commit()
    conn.close()

# id
# telegramid
# date_add