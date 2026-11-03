
students = []

def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    name = input("Enter student name: ").strip()

    try:
        mark = float(input("Enter mark: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if not name or mark < 0 or mark > 100:
        print("Invalid name or mark!")
        return

    students.append({
        "name": name,
        "mark": mark,
        "grade": get_grade(mark)
    })

    print("Student added successfully!")


def show_results():
    if not students:
        print("No students found!")
        return

    print("\nName         Mark   Grade")

    marks = []

    for student in students:
        print(f"{student['name']:<13}{student['mark']:>5.0f}{student['grade']:>8}")
        marks.append(student["mark"])

    average = sum(marks) / len(marks)

    print(
        f"Average: {average:.1f}    "
        f"Highest: {max(marks):.0f}    "
        f"Lowest: {min(marks):.0f}"
    )


while True:
    print("\n===== STUDENT GRADE MANAGER =====")
    print("1. Add Student")
    print("2. Show Results")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_results()

    elif choice == "3":
        print("Program closed.")
        break

    else:
        print("Invalid choice!")
