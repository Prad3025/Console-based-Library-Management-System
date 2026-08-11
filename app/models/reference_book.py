from models.book import Book
from exceptions import BookUnavailableException


class ReferenceBook(Book):

    def issue(self):
        raise BookUnavailableException(
            f"Reference book '{self.title}' cannot be issued"
        )

    def reference_only(self):
        print(
            f"'{self.title}' is for reference only."
        )