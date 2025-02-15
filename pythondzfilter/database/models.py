import sqlite3


def make_table():
    with sqlite3.connect('food_drinks.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            id integer primary key,
            user_id biginteger,
            food_name TEXT,
            food_size TEXT,
            drink_name TEXT,
            drink_size TEXT
        )
        """)
        conn.commit()