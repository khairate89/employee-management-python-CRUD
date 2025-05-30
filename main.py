from employee_app import add_employee, list_employees, update_employee, delete_employee

def menu():
    while True:
        print("\n--- Employee Management ---")
        print("1. List Employees")
        print("2. Add Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            list_employees()
            print("Done.")
        elif choice == '2':
            name = input("Name: ")
            dept = input("Department: ")
            salary = float(input("Salary: "))
            add_employee(name, dept, salary)
        elif choice == '3':
            emp_id = int(input("Employee ID: "))
            name = input("New Name: ") or None
            dept = input("New Department: ") or None
            salary = input("New Salary: ")
            salary = float(salary) if salary else None
            update_employee(emp_id, name, dept, salary)
        elif choice == '4':
            emp_id = int(input("Employee ID: "))
            delete_employee(emp_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
