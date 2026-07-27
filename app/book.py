class Book:

    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status

    def display(self):
        print(f"""
Book ID : {self.book_id}
Title   : {self.title}
Author  : {self.author}
Status  : {self.status}
""")

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "status": self.status
        }