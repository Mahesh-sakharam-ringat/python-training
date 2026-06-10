from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

##app = Flask(__name__)
##app = Flask(__name__, template_folder='templates')  
app = Flask(__name__, template_folder='../templates')
app.secret_key = "smartexam"

students = [
    {
        "roll": 101,
        "name": "mahesh",
        "score": 2,
        "percentage": 66.67,
        "date": "03-06-2026",
        "status": "Pass"
    },
    {
        "roll": 102,
        "name": "Priya",
        "score": 3,
        "percentage": 100,
        "date": "03-06-2026",
        "status": "Pass"
    },
    {
        "roll": 103,
        "name": "Amit",
        "score": 1,
        "percentage": 33.33,
        "date": "03-06-2026",
        "status": "Fail"
    }
]


@app.route('/')
def home():
    total = len(students)
    passed = len([s for s in students if s["status"] == "Pass"])
    failed = len([s for s in students if s["status"] == "Fail"])

    return render_template(
        'home.html',
        total=total,
        passed=passed,
        failed=failed
    )


@app.route('/record')
def record():
    return render_template('record.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':

        name = request.form['name']
        marks = int(request.form['marks'])

        percentage = (marks / 3) * 100
        status = "Pass" if marks >= 2 else "Fail"

        student = {
            "roll": 100 + len(students) + 1,
            "name": name,
            "score": marks,
            "percentage": round(percentage, 2),
            "date": datetime.now().strftime("%d-%m-%Y"),
            "status": status
        }

        students.append(student)

        flash(f"Student {name} added successfully!")

        return redirect(url_for('record'))

    return render_template('add_student.html')


if __name__ == '__main__':
    app.run(debug=True)