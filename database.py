import sqlite3

def connect():
    return sqlite3.connect("news_data.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            headline TEXT,
            scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(news_list):
    conn = connect()
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO news (headline) VALUES (?)', news_list)
    conn.commit()
    conn.close()
