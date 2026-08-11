from exceptions import BookUnavailableException


class Book:

    def __init__(
        self,
        book_id,
        isbn,
        title,
        author,
        category,
        copies_available,
        created_date
    ):
        self.book_id = book_id
        self.isbn = isbn
        self.title = title
        self.author = author
        self.category = category
        self.copies_available = copies_available
        self.created_date = created_date

    def issue(self):
        if self.copies_available <= 0:
            raise BookUnavailableException(
                f"Book '{self.title}' is unavailable"
            )

        self.copies_available -= 1

    def return_book(self):
        self.copies_available += 1

    def display(self):
        print(
            f"ID: {self.book_id}\n"
            f"ISBN: {self.isbn}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Category: {self.category}\n"
            f"Copies: {self.copies_available}\n"
            f"Created: {self.created_date}"
        )

    def __str__(self):
        return (
            f"{self.book_id} | "
            f"{self.title} | "
            f"{self.author} | "
            f"{self.category} | "
            f"Copies: {self.copies_available}"
        )