from flask import Flask, render_template, request, redirect, session, url_for, flash
from database import *
from database import init_db,get_db
from werkzeug.security import generate_password_hash, check_password_hash

##app = Flask(__name__)  # Specify the templates folder
##app = Flask(_name_, template_folder='templates')
app = Flask(__name__, template_folder='../templates')


app.secret_key = 'coaching_manager'  # Required for session management

create_tables()

# HOME
@app.route('/')
def home():
    return render_template('home.html')

# ---------------- STUDENTS ----------------

@app.route('/students')
def students():
    conn = get_db()
    data = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template('students.html', students=data)

@app.route('/add_student', methods=['GET','POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        subject = request.form['subject']
        contact = request.form['contact']
        admission_date = request.form['admission_date']

        conn = get_db()

        conn.execute("""
        INSERT INTO students
        (student_id,name ,subject,contact,admission_date)
        VALUES (?,?,?,?,?)
        """,(student_id,name,subject,contact,admission_date))

        conn.commit()
        conn.close()

        return redirect('/students')

    return render_template('add_student.html')

@app.route('/delete_student/<int:id>')
def delete_student(id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id=?",(id,))
    conn.commit()
    conn.close()

    return redirect('/students')

# ---------------- TEACHERS ----------------

@app.route('/teachers')
def teachers():
    conn = get_db()
    data = conn.execute("SELECT * FROM teachers").fetchall()
    conn.close()

    return render_template('teachers.html', teachers=data)

@app.route('/add_teacher', methods=['GET','POST'])
def add_teacher():

    if request.method == 'POST':
        teacher_id = request.form['teacher_id']
        teacher_name = request.form['teacher_name']
        subject = request.form['subject']
        contact = request.form['contact']

        conn = get_db()

        conn.execute("""
        INSERT INTO teachers
        (teacher_id,teacher_name,subject,contact)
        VALUES (?,?,?,?)
        """,(teacher_id,teacher_name,subject,contact))

        conn.commit()
        conn.close()

        return redirect('/teachers')

    return render_template('add_teacher.html')

@app.route('/delete_teacher/<int:id>')
def delete_teacher(id):
    conn = get_db()
    conn.execute("DELETE FROM teachers WHERE id=?",(id,))
    conn.commit()
    conn.close()

    return redirect('/teachers')    

# ---------------- subjects ----------------

@app.route('/subjects')
def subjects():
    conn = get_db()
    data = conn.execute("SELECT * FROM subjects").fetchall()
    conn.close()

    return render_template('subjects.html', subjects=data)

@app.route('/add_subjects', methods=['GET','POST'])
def add_subjects():

    if request.method == 'POST':
        subject_id = request.form['subject_id']
        subject_name = request.form['subject_name']
        duration = request.form['duration']
        fees = request.form['fees']

        conn = get_db()

        conn.execute("""
        INSERT INTO subjects
        (subject_id,subject_name,duration,fees)
        VALUES (?,?,?,?)
        """,(subject_id,subject_name,duration,fees))

        conn.commit()
        conn.close()

        return redirect('/subjects')

    return render_template('add_subjects.html')

# ---------------- SEARCH ----------------

@app.route('/search', methods=['GET', 'POST'])
def search():
    
    result = None
#step 1 - get query from URL
    
    q = request.args.get('q','')
    # request.args - GET parameters
    # 'q' - Form  - name = 'q'
    conn = get_db()
    

    if request.method == 'POST':
        category = request.form['category']
        search_by = request.form['search_by']
        search_value = request.form['search_value']

        # Add your search logic here

    return render_template('search.html', result=result)



 #******filter*****

@app.route('/filter')
def filter_students():
    #Values from URL
    subject = request.args.get('subject', '')
    grade = request.args.get('grade', '')

    conn = get_db()
    # Unique subjects for dropdown
    subjects = conn.execute('''SELECT DISTINCT subject FROM students
                            WHERE subject IS NOT NULL
                            AND subject != ""
                            ORDER BY subject ASC''').fetchall()  
    subjects = [subject[0] for subject in subjects]
    subjects.insert(0, '')
    conn.close()  
    
    # Dynamically build query based on filters
        
    query = 'SELECT * FROM students WHERE 1=1'
    params = []

    if subject:
        query += ' AND subject = ?'
        params.append(subject)

    if grade:
        query += ' AND grade = ?'
        params.append(grade)

    conn = get_db()
    query += ' ORDER BY id DESC'
    students = conn.execute(query, params).fetchall()
    conn.close()
    return render_template('filter.html', students=students, subjects=subjects, selected_subject=subject, selected_grade=grade)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        role = request.form['role']

        conn = get_db()
        hashed_password = generate_password_hash(password)
        conn.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, hashed_password, role))
        conn.commit()
        conn.close()

        flash('User registered successfully!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        role = request.form['role']

        conn = get_db()
        hashed_password = generate_password_hash(password)
        conn.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, hashed_password, role))
        conn.commit()
        conn.close()

        flash('User registered successfully!', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        
        conn = get_db()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            session['role'] = user['role']
            flash(f'Welcome {username}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    
    session.pop('username', None)
    session.pop('role', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


init_db()  # Initialize the database and create tables if they don't exist
if __name__ == '__main__':
 
 app.run(debug=True)