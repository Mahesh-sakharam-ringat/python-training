# Coaching Class Manager

# Main Entity Dictionary
coaching_class = {
    "class_name": "Bright Future Academy",
    "owner": "Mahesh Patil",
    "location": "Pune",
    "contact": "9876543210",
    "total_students": 5,
    "total_teachers": 4
}

# Student Records (List of Dictionaries)
students = [
    {"id": 1, "name": "Rahul", "course": "Python", "fees": 5000, "paid": 5000},
    {"id": 2, "name": "Sneha", "course": "Java", "fees": 6000, "paid": 4000},
    {"id": 3, "name": "Amit", "course": "C++", "fees": 4500, "paid": 4500},
    {"id": 4, "name": "Pooja", "course": "Python", "fees": 5000, "paid": 3000},
    {"id": 5, "name": "Rohit", "course": "Java", "fees": 6000, "paid": 6000}
]

# Second Dictionary Type (Teachers)
teachers = {
    "T101": "Mr. Sharma",
    "T102": "Mrs. Joshi",
    "T103": "Mr. Patil",
    "T104": "Ms. Kulkarni"
}

# Function to check fee status
def get_status(fees, paid):
    if paid >= fees:
        return "Fees Paid"
    else:
        return "Remaining Fees"

# Function to search student by name
def search_records(student_name):
    found = False

    for student in students:
        if student["name"].lower() == student_name.lower():
            print("\nStudent Found:")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Fees:", student["fees"])
            print("Paid:", student["paid"])
            print("Remaining:", student["fees"] - student["paid"])
            found = True

    if not found:
        print("Student not found!")

# Display Coaching Class Information
print("===== COACHING CLASS DETAILS =====")
for key, value in coaching_class.items():
    print(key, ":", value)

# Display Teacher Information
print("\n===== TEACHERS =====")
for teacher_id, teacher_name in teachers.items():
    print(teacher_id, "-", teacher_name)

# Display Student Information
print("\n===== STUDENT DETAILS =====")
for student in students:
    remaining = student["fees"] - student["paid"]

    print("\nID:", student["id"])
    print("Name:", student["name"])
    print("Course:", student["course"])
    print("Total Fees:", student["fees"])
    print("Paid Fees:", student["paid"])
    print("Remaining Fees:", remaining)
    print("Status:", get_status(student["fees"], student["paid"]))

# Search Student
name = input("\nEnter student name to search: ")
search_records(name)