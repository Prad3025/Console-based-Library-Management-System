from book import Book

class DigitalBook(Book):

    def __init__(self, book_id, title, author, file_size, status="Available"):
        super().__init__(book_id, title, author, status)
        self.file_size = file_size

    def display(self):
        super().display()
        print(f"File Size : {self.file_size}")