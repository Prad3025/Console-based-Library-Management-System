class IssueTransaction:

    def __init__(
        self,
        transaction_id,
        book_id,
        member_id,
        issue_date,
        return_date,
        status
    ):
        self.transaction_id = transaction_id
        self.book_id = book_id
        self.member_id = member_id
        self.issue_date = issue_date
        self.return_date = return_date
        self.status = status

    def display(self):
        print(
            f"Transaction ID: {self.transaction_id}\n"
            f"Book ID: {self.book_id}\n"
            f"Member ID: {self.member_id}\n"
            f"Issue Date: {self.issue_date}\n"
            f"Return Date: {self.return_date}\n"
            f"Status: {self.status}"
        )

    def __str__(self):
        return (
            f"{self.transaction_id} | "
            f"Book: {self.book_id} | "
            f"Member: {self.member_id} | "
            f"Issued: {self.issue_date} | "
            f"Returned: {self.return_date} | "
            f"{self.status}"
        )