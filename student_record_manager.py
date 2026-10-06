import re

FILE_NAME = "students.txt"


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        email = input("Enter Email: ")

        if not validate_email(email):
            raise ValueError("Invalid email format!")

        with open(FILE_NAME, "a") as file:
            file.write(f"{student_id},{name},{age},{email}\n")

        print("Student added successfully!")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Something went wrong:", e)


def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No student records found.")
                return

            print("\n--- Student Records ---")

            for line in data:
                student_id, name, age, email = line.strip().split(",")

                print("Student ID:", student_id)
                print("Name:", name)
                print("Age:", age)
                print("Email:", email)
                print("----------------------")

    except FileNotFoundError:
        print("No student data file found.")
    except Exception as e:
        print("Error:", e)


while True:
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. Read Student Data")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            read_students()
        elif choice == 3:
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    except ValueError:
        print("Invalid input! Please enter a number.")
