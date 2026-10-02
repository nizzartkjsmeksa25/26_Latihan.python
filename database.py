import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("database_nizzar.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pengguna (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            kelas TEXT,
            password TEXT,
            timer TEXT
        )
    ''')
    conn.commit()
    conn.close()

def simpan_data(nama, kelas, password):
    init_db()
    conn = sqlite3.connect("database_nizzar.db")
    cursor = conn.cursor()
    timer = datetime.now().strftime("%H:%M:%S")
    cursor.execute("INSERT INTO pengguna (nama, kelas, password, timer) VALUES (?, ?, ?, ?)", 
                   (nama, kelas, password, timer))
    conn.commit()
    conn.close()
    return timer
