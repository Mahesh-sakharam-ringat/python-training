import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'sanklap_secret_key'

def get_db():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    mark INTEGER default 0
                )''')
    conn.commit()
    conn.close()

    @app.route('/')
    def home():
        conn = get_db()
        students = conn.execute('SELECT * FROM students ORDER BY mark DESC').fetchall()
        conn.close()
        return render_template('home.html', students=students)
    
    def add_student():
        if request.method == 'POST':
            name = request.form['name']
            mark = request.form['mark']
            conn = get_db()
            conn.execute('INSERT INTO students (name, mark) VALUES (?, ?)', (name, mark))
            conn.commit()
            conn.close()
            flash('Student added successfully!')
        return redirect(url_for('home'))
    
    conn = get_db()
    conn.execute('INSERT INTO students (name, mark) VALUES (?, ?)', ('Alice', 85))
    conn.execute('INSERT INTO students (name, mark) VALUES (?, ?)', ('Bob', 90))
    conn.execute('INSERT INTO students (name, mark) VALUES (?, ?)', ('Charlie', 78))
    conn.commit()
    conn.close()

    print(f"Received new student : {name} with marks :{mark}")

    flash(f"student {name} added successfully with marks {mark}!")

    return render_template("add_student.html")

@app.route("/delete/<int:student_id>")
def delete_student(student_id):
    conn = get_db()
    conn.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    flash(f'Student deleted successfully!')
    return redirect(url_for('home'))
