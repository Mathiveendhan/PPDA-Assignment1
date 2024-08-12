from employee_management import EmployeeManagementSystem

if __name__ == "__main__":
    ems = EmployeeManagementSystem()

    # Adding Employees
    ems.add_employee("Rahul", "rahul@example.com", "Networking Engineer", 200000)
    ems.add_employee("Jasim Ahamad", "jasim.@example.com", "Security analyst", 95000)
    ems.add_employee("Nesan", "nesan@gmail.com", "ML Engineer",190000)

    # Updating Employee Information
    ems.update_employee("1", job_title="Senior Networking Engineer", base_salary=200000)

    # Adding Performance Metrics
    ems.add_performance_metric("1", "Project Success", 9.0)
    ems.add_performance_metric("2", "Team Leadership", 8.5)
    ems.add_performance_metric("3", "Quality Reports", 9.5)

    # Calculating Salaries with Bonus
    ems.calculate_salary("1", performance_weight=1000)
    ems.calculate_salary("2", performance_weight=1200)
    ems.calculate_salary("3", performance_weight=2200)
