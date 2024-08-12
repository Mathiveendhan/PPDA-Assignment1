class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = {}

    def add_course(self, course_name, grade=None):
        self.courses[course_name] = grade

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'email': self.email,
            'courses': self.courses
        }

    @staticmethod
    def from_dict(data):
        student = Student(data['student_id'], data['name'], data['email'])
        student.courses = data['courses']
        return student
