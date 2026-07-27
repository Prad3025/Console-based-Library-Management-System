from member import Member

class Faculty(Member):

    def __init__(self, member_id, name, department):
        super().__init__(member_id, name)
        self.department = department