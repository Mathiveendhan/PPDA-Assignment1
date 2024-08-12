from student_management import StudentManagementSystem

if __name__ == "__main__":
    sms = StudentManagementSystem()

    # Adding Students
    sms.add_student("Mathiveendhan","mathiveendhan003@gmail.com")
    sms.add_student("mathinesan","mathinesanpalanisamy@gmail.com")
    sms.add_student("bharaniraja","bharaniraja123@gmail.com")

    # Adding Courses
    sms.add_course("Artificial Intelligence")
    sms.add_course("Networking Security")
    sms.add_course("Data Structure in Java")


    # Enrolling Students in Courses
    sms.enroll_student_in_course("1", "1")  
    sms.enroll_student_in_course("2", "2") 
    sms.enroll_student_in_course("3","3")  
    sms.enroll_student_in_course("2", "3") 

    # Assigning Grades
    sms.assign_grade("1", "1", 90)  
    sms.assign_grade("2", "2", 85)  
    sms.assign_grade("3", "3", 67) 
    sms.assign_grade("2", "3", 76)

    # Calculating GPA
    sms.calculate_gpa("1") 
    sms.calculate_gpa("2")  
    sms.calculate_gpa("3") 
