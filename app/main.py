books = []


# Add Book
def add_book():
    print("\n----- Add Book -----")

    book = {
        "book_id": int(input("Enter Book ID: ")),
        "title": input("Enter Book Title: "),
        "author": input("Enter Author Name: "),
        "status": "Available"
    }

    books.append(book)

    print("\nBook added successfully!")


# View Books
def view_books():

    if len(books) == 0:
        print("\nNo books available in the library.")
        return

    print("\n========== Book Details ==========")

    for book in books:

        print(f"""
Book ID : {book["book_id"]}
Title   : {book["title"]}
Author  : {book["author"]}
Status  : {book["status"]}
""")


# Search Book
def search_book():

    if len(books) == 0:
        print("\nNo books available in the library.")
        return

    search_title = input("Enter Book Title to Search: ")

    found = False

    for book in books:

        if book["title"].lower() == search_title.lower():

            print("\nBook Found")

            print(f"""
Book ID : {book["book_id"]}
Title   : {book["title"]}
Author  : {book["author"]}
Status  : {book["status"]}
""")

            found = True
            break

    if not found:
        print("\nBook not found.")


# Delete Book
def delete_book():

    if len(books) == 0:
        print("\nNo books available in the library.")
        return

    delete_id = int(input("Enter Book ID to Delete: "))

    found = False

    for book in books:

        if book["book_id"] == delete_id:

            books.remove(book)

            print("\nBook deleted successfully!")

            found = True
            break

    if not found:
        print("\nBook ID not found.")


# Issue Book
def issue_book():

    if len(books) == 0:
        print("\nNo books available in the library.")
        return

    issue_id = int(input("Enter Book ID to Issue: "))

    found = False

    for book in books:

        if book["book_id"] == issue_id:

            found = True

            if book["status"] == "Available":

                book["status"] = "Issued"

                print("\nBook issued successfully!")

            else:

                print("\nBook is already issued.")

            break

    if not found:
        print("\nBook ID not found.")


# Return Book
def return_book():

    if len(books) == 0:
        print("\nNo books available in the library.")
        return

    return_id = int(input("Enter Book ID to Return: "))

    found = False

    for book in books:

        if book["book_id"] == return_id:

            found = True

            if book["status"] == "Issued":

                book["status"] = "Available"

                print("\nBook returned successfully!")

            else:

                print("\nBook is already available.")

            break

    if not found:
        print("\nBook ID not found.")


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
            print("\nInvalid choice. Please enter a number between 1 and 7.")

    except ValueError:
        print("\nPlease enter numbers only.")