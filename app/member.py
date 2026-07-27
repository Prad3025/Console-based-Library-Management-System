class Member:
    def __init__(self, member_id,name):
        self.member_id=member_id
        self.name=name

    def display(self):
        print(f"""Member ID : {self.member_id}
Name    : {self.name}
""")