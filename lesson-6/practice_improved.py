def show_menu():
    print("""
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
""")
    
def new_employee():
    with open('employees111.txt', 'a') as file:
        employee_id = input("Enter Employee ID: ")
        name = input("Please enter the Employee Name: ")
        position = input("Please enter the Employee Position: ")
        salary = input("Please enter the Employee Salary: ")
        record = f'{employee_id}, {name}, {position}, {salary}\n'
        file.write(record)
    print("Employee information recorded successfully!\n")

def all_view():
    try:
        with open('employees111.txt', 'r') as file:
            records = file.readlines()
            for i in records:
                print(i.strip())
    except FileNotFoundError:
        print("The file 'employees111.txt' does not exist")

def search_employee():
    search_id = input("Enter the Employee ID to search: ")
    found = False
    with open('employees111.txt', 'r') as file:
        for line in file:
            if line.startswith(search_id + ","):
                print("Employee Found: ", line.strip())
                found = True
    if not found:
        print("Employee not found")

def update_info():
    search_id = input("Enter the Employee ID to update: ")
    updated_record = []
    found = False
    with open('employees111.txt', 'r') as file:
        for line in file:
            if line.startswith(search_id + ","):
                print("Employee Found: ", line.strip())
                name = input("Please enter the Employee Name: ")
                position = input("Please enter the Employee Position: ")
                salary = input("Please enter the Employee Salary: ")
                updated_record.append(f'{search_id}, {name}, {position}, {salary}\n')
                found = True
            else:
                updated_record.append(line)
    if found:
        with open('employees111.txt', 'w') as file:
            file.writelines(updated_record)
        print("Employee record updated successfully!")
    else:
        print("Employee not found")

def delete_employee():
    search_id = input("Enter Employee ID to delete: ")
    updated_record = []
    found = False
    with open('employees111.txt', 'r') as file:
        for line in file:
            if not line.startswith(search_id + ","):
                updated_record.append(line)
            else:
                found = True
    if found:
        with open('employees111.txt', 'w') as file:
            file.writelines(updated_record)
        print("Employee record deleted successfully!\n")
    else:
        print("Employee not found!\n")

def menu():
    while True:
        show_menu()
        try:
            choice = int(input("Please choose an option: "))
            print()
            if choice == 1:
                new_employee()
            elif choice == 2:
                all_view()
            elif choice == 3:
                search_employee()
            elif choice == 4:
                update_info()
            elif choice == 5:
                delete_employee()
            elif choice == 6:
                print("Thank you for using the program!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 6.\n")
        except ValueError:
            print("Invalid input! Please enter a number.\n")


if __name__ == "__main__":
    menu()