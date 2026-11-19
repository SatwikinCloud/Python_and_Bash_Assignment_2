
students = {
    "Rahul": "A",
    "Aman": "B",
    "Priya": "A"
}

while True:
    print("\n--- Student Grade Management ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Display All Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")

        if name in students:
            print("Student already exists!")
        else:
            students[name] = grade
            print("Student added successfully!")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated successfully!")
        else:
            print("Student not found!")

    elif choice == "3":
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
