class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def to_dict(self):
        return {
            'course_id': self.course_id,
            'course_name': self.course_name
        }

    @staticmethod
    def from_dict(data):
        return Course(data['course_id'], data['course_name'])
