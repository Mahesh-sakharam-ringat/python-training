from flask import Flask, render_template, request, redirect

##app = Flask(__name__)
##app = Flask(__name__, template_folder='templates')
app = Flask(__name__, template_folder='../templates')

students = [
    {
        "id": "S101",
        "name": "Rahul Patil",
        "contact": "9876543210",
        "course": "Python",
        "admission_date": "01-06-2026"
    }
]

teachers = [
    {
        "id": "T101",
        "name": "Amit Sir",
        "subject": "Python",
        "contact": "9876541111"
    }
]

courses = [
    {
        "id": "C101",
        "name": "Python",
        "duration": "3 Months",
        "fees": 5000
    }
]


@app.route('/')
def home():
    return render_template(
        'home.html',
        total_students=len(students),
        total_teachers=len(teachers),
        total_courses=len(courses)
    )


@app.route('/students', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        students.append({
            "id": request.form['id'],
            "name": request.form['name'],
            "contact": request.form['contact'],
            "course": request.form['course'],
            "admission_date": request.form['admission_date']
        })
        return redirect('/students')

    return render_template('students.html', students=students)


@app.route('/teachers', methods=['GET', 'POST'])
def teacher():
    if request.method == 'POST':
        teachers.append({
            "id": request.form['id'],
            "name": request.form['name'],
            "subject": request.form['subject'],
            "contact": request.form['contact']
        })
        return redirect('/teachers')

    return render_template('teachers.html', teachers=teachers)


@app.route('/courses', methods=['GET', 'POST'])
def course():
    if request.method == 'POST':
        courses.append({
            "id": request.form['id'],
            "name": request.form['name'],
            "duration": request.form['duration'],
            "fees": request.form['fees']
        })
        return redirect('/courses')

    return render_template('courses.html', courses=courses)


@app.route('/search', methods=['GET', 'POST'])
def search():
    result = None

    if request.method == 'POST':
        keyword = request.form['keyword'].lower()

        result = []

        for s in students:
            if keyword in s['id'].lower() or keyword in s['name'].lower():
                result.append(s)

        for t in teachers:
            if keyword in t['name'].lower():
                result.append(t)

    return render_template('search.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
