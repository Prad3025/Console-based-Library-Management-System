from storage import save_books,load_books
from exceptions import BookNotFound

books = load_books()

def add_book():
    print("\n----- Add Book -----")

    try:
        book_id = int(input("Enter Book ID: "))
    except ValueError:
        print("Book ID must be a number.")
        return

    for book in books:
        if book["book_id"] == book_id:
            print("Book ID already exists.")
            return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    save_books(books)

    print("\nBook added successfully!")


# View Books
def view_books():

    if not books:
        print("\nNo books available.")
        return

    print("\n========== Book Details ==========")

    for book in sorted(books,key=lambda x: x['title']):
        print(f"""
Book ID : {book["book_id"]}
Title   : {book["title"]}
Author  : {book["author"]}
Status  : {book["status"]}
""")


# Search Book
def search_book():

    if not books:
        print("\nNo books available.")
        return

    search = input("Enter Book Title or Book ID: ")

    try:
        for book in books:
                if (str(book["book_id"])==search or book["title"].lower()==search.lower()):
                    print("\n Book found")
                

                    print(f"""
Book ID : {book["book_id"]}
Title   : {book["title"]}
Author  : {book["author"]}
Status  : {book["status"]}
""")
                    return

        raise BookNotFound("Book not found.")

    except BookNotFound as e:
        print(e)


# Delete Book
def delete_book():

    if not books:
        print("\nNo books available.")
        return

    try:
        delete_id = int(input("Enter Book ID to Delete: "))

        for book in books:
            if book["book_id"] == delete_id:
                books.remove(book)
                save_books(books)
                print("Book deleted successfully!")
                return

        raise BookNotFound("Book ID not found.")

    except ValueError:
        print("Please enter a valid number.")

    except BookNotFound as e:
        print(e)


# Issue Book
def issue_book():

    if not books:
        print("\nNo books available.")
        return

    try:
        issue_id = int(input("Enter Book ID to Issue: "))

        for book in books:

            if book["book_id"] == issue_id:

                if book["status"] == "Available":
                    book["status"] = "Issued"
                    save_books(books)
                    print("Book issued successfully!")

                else:
                    print("Book is already issued.")

                return

        raise BookNotFound("Book ID not found.")

    except ValueError:
        print("Please enter a valid number.")

    except BookNotFound as e:
        print(e)


# Return Book
def return_book():

    if not books:
        print("\nNo books available.")
        return

    try:
        return_id = int(input("Enter Book ID to Return: "))

        for book in books:

            if book["book_id"] == return_id:

                if book["status"] == "Issued":
                    book["status"] = "Available"
                    save_books(books)
                    print("Book returned successfully!")

                else:
                    print("Book is already available.")

                return

        raise BookNotFound("Book ID not found.")

    except ValueError:
        print("Please enter a valid number.")

    except BookNotFound as e:
        print(e)