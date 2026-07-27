from book import Book

class ReferenceBook(Book):

    def __init__(self, book_id, title, author, status="Available"):
        super().__init__(book_id, title, author, status)

    def issue_book(self):
        print("Reference books cannot be issued.")