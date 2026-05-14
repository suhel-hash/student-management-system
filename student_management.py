students = {}

while True:
    print("\n---Student Management System---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter student marks: ")
        students[name] = marks
        print("Student added successfully!")


    elif choice == "2":
        print("\nstudent Records:")

        if len(students) == 0:
            print("NO student records found.")

        else:
            for name, marks in students.items():
                print(f"Name: {name}, Marks: {marks}")


    elif choice == "3":

        search = input("Enter student name to search: ")

        if search in students:
            print(f"{search}'s Marks: {students[search]}")

        else:
            print("Student not found!")


    elif choice == "4":

        print("Exiting program---")
        break
        
    else:
        print("Invalid choice!")
    
