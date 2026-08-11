from models.member import Member


class Faculty(Member):

    def __init__(
        self,
        member_id,
        name,
        email,
        status
    ):
        super().__init__(
            member_id,
            name,
            email,
            "Faculty",
            status
        )