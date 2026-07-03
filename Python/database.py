import os
import sqlite3
from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = 'your_secret_key'

#absolute path - always with app.py folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'coaching_manager.db')
def get_db():
    """Database connection """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        name TEXT,
        contact TEXT,
        subject TEXT,
        admission_date TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS teachers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id TEXT,
        teacher_name TEXT,
        subject TEXT,
        contact TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS subjects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id TEXT,
        subject_name TEXT,
        duration TEXT,
        fees INTEGER
    )
    """)

    conn.execute('''
                 CREATE TABLE IF NOT EXISTS users (
                 
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                 )
                    ''')    
    



    conn.commit()
    conn.close()
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        name TEXT,
        contact TEXT,
        subject TEXT,
        admission_date TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS teachers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id TEXT,
        teacher_name TEXT,
        subject TEXT,
        contact TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS subjects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id TEXT,
        subject_name TEXT,
        duration TEXT,
        fees INTEGER
    )
    """)

    conn.execute('''
                 CREATE TABLE IF NOT EXISTS users (
                 
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                 )
                    ''')    
    



    conn.commit()
    conn.close()

init_db() #initialize the database and create tables if they don't exist   
if __name__ == "__main__":
    app.run(debug=True)