from member import Member

class Student(Member):

    def __init__(self, member_id, name, course):
        super().__init__(member_id, name)
        self.course = course