import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"
    
    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'w'):
                pass  # Create file if it does not exist

    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        if self.search_employee(employee_id):
            print("Employee ID already exists. Please enter a unique ID.")
            return
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        with open(self.FILE_NAME, "a") as file:
            file.write(f"{employee_id},{name},{position},{salary}\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        with open(self.FILE_NAME, "r") as file:
            records = file.readlines()
            if not records:
                print("No employee records found.")
                return
            print("Employee Records:")
            for record in records:
                print(record.strip())
    
    def search_employee(self, employee_id):
        with open(self.FILE_NAME, "r") as file:
            for record in file:
                emp_data = record.strip().split(",")
                if emp_data[0] == employee_id:
                    return Employee(*emp_data)
        return None
    
    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")
        employees = []
        found = False
        with open(self.FILE_NAME, "r") as file:
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
        with open(self.FILE_NAME, "w") as file:
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
                self.view_all_employees()
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