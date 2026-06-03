from flask import Flask

from flask import Flask


app = Flask(__name__)

# List of dictionaries (5 records)
students = [
    {"id": 1, "name": "Kartik", "course": "Computer Engineering", "status": "Active"},
    {"id": 2, "name": "Priya", "course": "IT", "status": "Active"},
    {"id": 3, "name": "Amit", "course": "Mechanical", "status": "Inactive"},
    {"id": 4, "name": "Sneha", "course": "Civil", "status": "Active"},
    {"id": 5, "name": "Rohan", "course": "Electrical", "status": "Active"}
]

# Route 1 - Homepage
@app.route("/")
def home():
    return """
    <h1>coaching class manager</h1>
    <p>This project manages student records and their status.</p>
    """

# Route 2 - Records Page
@app.route("/records")
def records():
    output = "<h2>Student Records</h2>"
    
    for student in students:
        output += f"""
        <p>
        ID: {student['id']} <br>
        Name: {student['name']} <br>
        Course: {student['course']} <br>
        Status: {student['status']}
        </p>
        <hr>
        """
    
    return output

# Route 3 - Extra Route
@app.route("/active")
def active_students():
    output = "<h2>Active Students</h2>"
    
    for student in students:
        if student["status"] == "Active":
            output += f"<p>{student['name']} - {student['course']}</p>"
    
    return output

if __name__ == "__main__":
    app.run(debug=True)