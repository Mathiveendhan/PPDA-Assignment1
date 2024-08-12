import os
import json
from student import Student
from course import Course

class StudentManagementSystem:
    def __init__(self, students_file='students.json', courses_file='courses.json'):
        self.students_file = students_file
        self.courses_file = courses_file
        self.students = self.load_students()
        self.courses = self.load_courses()

    def load_students(self):
        if os.path.exists(self.students_file):
            with open(self.students_file, 'r') as file:
                return {student_id: Student.from_dict(student) for student_id, student in json.load(file).items()}
        return {}

    def load_courses(self):
        if os.path.exists(self.courses_file):
            with open(self.courses_file, 'r') as file:
                return {course_id: Course.from_dict(course) for course_id, course in json.load(file).items()}
        return {}

    def save_students(self):
        with open(self.students_file, 'w') as file:
            json.dump({student_id: student.to_dict() for student_id, student in self.students.items()}, file)

    def save_courses(self):
        with open(self.courses_file, 'w') as file:
            json.dump({course_id: course.to_dict() for course_id, course in self.courses.items()}, file)

    def add_student(self, name, email):
        student_id = str(len(self.students) + 1)
        new_student = Student(student_id, name, email)
        self.students[student_id] = new_student
        self.save_students()
        print(f"Student '{name}' added successfully with ID {student_id}.")

    def add_course(self, course_name):
        course_id = str(len(self.courses) + 1)
        new_course = Course(course_id, course_name)
        self.courses[course_id] = new_course
        self.save_courses()
        print(f"Course '{course_name}' added successfully with ID {course_id}.")

    def enroll_student_in_course(self, student_id, course_id):
        if student_id not in self.students or course_id not in self.courses:
            print("Invalid student ID or course ID.")
            return
        student = self.students[student_id]
        course = self.courses[course_id]
        student.add_course(course.course_name)
        self.save_students()
        print(f"Student '{student.name}' enrolled in course '{course.course_name}' successfully.")

    def assign_grade(self, student_id, course_id, grade):
        if student_id not in self.students or course_id not in self.courses:
            print("Invalid student ID or course ID.")
            return
        student = self.students[student_id]
        course = self.courses[course_id]
        if course.course_name in student.courses:
            student.courses[course.course_name] = grade
            self.save_students()
            print(f"Grade '{grade}' assigned to student '{student.name}' for course '{course.course_name}'.")
        else:
            print(f"Student '{student.name}' is not enrolled in course '{course.course_name}'.")

    def calculate_gpa(self, student_id):
        if student_id not in self.students:
            print("Invalid student ID.")
            return
        student = self.students[student_id]
        grades = [grade for grade in student.courses.values() if grade is not None]
        if not grades:
            print(f"No grades available for student '{student.name}'.")
            return
        gpa = sum(grades) / len(grades)
        print(f"Student '{student.name}' has a GPA of {gpa:.2f}.")

