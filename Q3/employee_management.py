import os
import json
from employee import Employee

class EmployeeManagementSystem:
    def __init__(self, employees_file='employees.json'):
        self.employees_file = employees_file
        self.employees = self.load_employees()

    def load_employees(self):
        if os.path.exists(self.employees_file):
            with open(self.employees_file, 'r') as file:
                return {employee_id: Employee.from_dict(employee) for employee_id, employee in json.load(file).items()}
        return {}

    def save_employees(self):
        with open(self.employees_file, 'w') as file:
            json.dump({employee_id: employee.to_dict() for employee_id, employee in self.employees.items()}, file)

    def add_employee(self, name, email, job_title, base_salary):
        employee_id = str(len(self.employees) + 1)
        new_employee = Employee(employee_id, name, email, job_title, base_salary)
        self.employees[employee_id] = new_employee
        self.save_employees()
        print(f"Employee '{name}' added successfully with ID {employee_id}.")

    def update_employee(self, employee_id, job_title=None, base_salary=None):
        if employee_id not in self.employees:
            print("Invalid employee ID.")
            return
        employee = self.employees[employee_id]
        employee.update_job_info(job_title, base_salary)
        self.save_employees()
        print(f"Employee '{employee.name}' record updated successfully.")

    def add_performance_metric(self, employee_id, metric_name, value):
        if employee_id not in self.employees:
            print("Invalid employee ID.")
            return
        employee = self.employees[employee_id]
        employee.add_performance_metric(metric_name, value)
        self.save_employees()
        print(f"Performance metric '{metric_name}' added for employee '{employee.name}'.")

    def calculate_salary(self, employee_id, performance_weight=0.1):
        if employee_id not in self.employees:
            print("Invalid employee ID.")
            return
        employee = self.employees[employee_id]
        bonus = employee.calculate_bonus(performance_weight)
        total_salary = employee.base_salary + bonus
        print(f"Total salary for employee '{employee.name}' is {total_salary:.2f} with a bonus of {bonus:.2f}.")
