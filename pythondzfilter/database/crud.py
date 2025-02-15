import sqlite3


def insert_food_drinks_to_table(user_id, food_name, food_size, drink_name, drink_size):
    with sqlite3.connect('food_drinks.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO orders(user_id, food_name, food_size, drink_name, drink_size) VALUES(?, ?, ?, ?, ?)', (user_id, food_name, food_size, drink_name, drink_size))
        conn.commit()