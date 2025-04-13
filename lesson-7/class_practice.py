import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f'{self.employee_id}, {self.name}, {self.position}, {self.salary}'
    
class EmployeeManager:
    file_name = "employeesclass.txt"

    def __init__(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w'):
                pass
    
    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        name = input("Please enter the Employee Name: ")
        position = input("Please enter the Employee Position: ")
        salary = input("Please enter the Employee Salary: ")

        with open(self.file_name, 'a') as file:
            file.write(f'{employee_id}, {name}, {position}, {salary}\n')
        print("Employee information recorded successfully!\n")

    def read_records(self):
        try:
            with open(self.file_name, 'r') as file:
                records = file.readlines()
                print("Employee records: ")
                for record in records:
                    print(record.strip())
        except FileNotFoundError:
            print("The file doesn't exist")
            return
    
    def search_employee(self, employee_id):
        with open(self.file_name, "r") as file:
            for record in file:
                emp_data = record.strip().split(",")
                if emp_data[0] == employee_id:
                    return Employee(*emp_data)
        return None
    
    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")
        employees = []
        found = False
        with open(self.file_name, "r") as file:
            for record in file:
                emp_data = record.strip().split(",")
                if emp_data[0] == employee_id:
                    found = True
                    name = input("Enter new Name: ") or emp_data[1]
                    position = input("Enter new Position: ") or emp_data[2]
                    salary = input("Enter new Salary: ") or emp_data[3]
                    employees.append(f"{employee_id},{name},{position},{salary}\n")
                else:
                    employees.append(record)
        if not found:
            print("Employee not found.")
            return
        with open(self.file_name, "w") as file:
            file.writelines(employees)
        print("Employee updated successfully!")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ")
        employees = []
        found = False
        with open(self.FILE_NAME, "r") as file:
            for record in file:
                if record.startswith(employee_id + ","):
                    found = True
                    continue
                employees.append(record)
        if not found:
            print("Employee not found.")
            return
        with open(self.FILE_NAME, "w") as file:
            file.writelines(employees)
        print("Employee deleted successfully!")
    
    def menu(self):
        while True:
            print("""
Welcome to the Employee Records Manager!
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
""")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.read_records()
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                employee = self.search_employee(employee_id)
                print(f"Employee Found:\n{employee}" if employee else "Employee not found.")
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()