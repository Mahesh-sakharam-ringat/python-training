# Coaching Class Manager

student_names = ["Mahesh", "Rahul", "Amit"]
total_fees = [10000, 12000, 15000]
paid_fees = [10000, 8000, 15000]

def display_students():
    print("**** Student Details ****")
    print("Name\tTotal Fees\tPaid Fees\tRemaining Fees\tStatus")

    for i in range(len(student_names)):
        remaining = total_fees[i] - paid_fees[i]

        if remaining == 0:
            status = "Fees Paid"
        else:
            status = "Fees Remaining"

        print(student_names[i], "\t", total_fees[i], "\t",
              paid_fees[i], "\t", remaining, "\t\t", status)

display_students()