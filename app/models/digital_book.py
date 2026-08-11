from models.book import Book


class DigitalBook(Book):

    def download(self):
        print(
            f"Downloading '{self.title}'..."
        )