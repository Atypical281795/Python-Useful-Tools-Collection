import sqlite3

def init_db():
    conn = sqlite3.connect('accounting.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS activities (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS entries (
                        id INTEGER PRIMARY KEY,
                        activity_id INTEGER NOT NULL,
                        item TEXT NOT NULL,
                        amount REAL NOT NULL,
                        claimant TEXT NOT NULL,
                        date TEXT NOT NULL,
                        attachment TEXT,
                        FOREIGN KEY (activity_id) REFERENCES activities (id))''')
    
    conn.commit()
    conn.close()

init_db()
