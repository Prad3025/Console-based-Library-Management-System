import json

# Custom Exception
class BookNotFound(Exception):
    pass


# Load Books from JSON
try:
    with open("books.json", "r") as file:
        books = json.load(file)
except FileNotFoundError:
    books = []

# Load Members from JSON
try:
    with open("members.json", "r") as file:
        members = json.load(file)
except FileNotFoundError:
    members = []


# Save Books
def save_books():
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)


# Add Book
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
    save_books()

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
                save_books()
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
                    save_books()
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
                    save_books()
                    print("Book returned successfully!")

                else:
                    print("Book is already available.")

                return

        raise BookNotFound("Book ID not found.")

    except ValueError:
        print("Please enter a valid number.")

    except BookNotFound as e:
        print(e)


# Main Menu
while True:

    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book()

        elif choice == 2:
            view_books()

        elif choice == 3:
            search_book()

        elif choice == 4:
            delete_book()

        elif choice == 5:
            issue_book()

        elif choice == 6:
            return_book()

        elif choice == 7:
            print("\nThank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

    except ValueError:
        print("Please enter numbers only.") 