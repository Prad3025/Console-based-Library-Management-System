class Member:

    def __init__(
        self,
        member_id,
        name,
        email,
        member_type,
        status
    ):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.member_type = member_type
        self.status = status

    def display(self):
        print(
            f"ID: {self.member_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Type: {self.member_type}\n"
            f"Status: {self.status}"
        )

    def __str__(self):
        return (
            f"{self.member_id} | "
            f"{self.name} | "
            f"{self.email} | "
            f"{self.member_type} | "
            f"{self.status}"
        )