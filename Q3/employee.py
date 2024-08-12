class Employee:
    def __init__(self, employee_id, name, email, job_title, base_salary):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.job_title = job_title
        self.base_salary = base_salary
        self.performance_metrics = {}

    def update_job_info(self, job_title=None, base_salary=None):
        if job_title:
            self.job_title = job_title
        if base_salary:
            self.base_salary = base_salary

    def add_performance_metric(self, metric_name, value):
        self.performance_metrics[metric_name] = value

    def calculate_bonus(self, performance_weight):
        total_score = sum(self.performance_metrics.values())
        bonus = total_score * performance_weight
        return bonus

    def to_dict(self):
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'email': self.email,
            'job_title': self.job_title,
            'base_salary': self.base_salary,
            'performance_metrics': self.performance_metrics
        }

    @staticmethod
    def from_dict(data):
        employee = Employee(
            data['employee_id'],
            data['name'],
            data['email'],
            data['job_title'],
            data['base_salary']
        )
        employee.performance_metrics = data['performance_metrics']
        return employee
