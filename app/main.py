from models.library import Library


library = Library()


def display_books(books):
    if not books:
        print("\nNo books found.")
        return

    print("\n===== BOOKS =====")

    for book in books:
        print(book)


def display_members(members):
    if not members:
        print("\nNo members found.")
        return

    print("\n===== MEMBERS =====")

    for member in members:
        print(member)


def add_book_menu():
    print("\n===== ADD BOOK =====")

    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    category = input("Enter category: ")
    copies = int(input("Enter number of copies: "))
    created_date = input("Enter created date (YYYY-MM-DD): ")

    try:
        library.add_book(
            isbn,
            title,
            author,
            category,
            copies,
            created_date
        )

        print("Book added successfully.")

    except Exception as e:
        print("Error:", e)


def search_book_menu():
    print("\n===== SEARCH BOOK =====")

    keyword = input("Enter title, author, or ISBN: ")

    try:
        books = library.search_books(keyword)
        display_books(books)

    except Exception as e:
        print("Error:", e)


def list_available_books_menu():
    print("\n===== AVAILABLE BOOKS =====")

    try:
        books = library.list_available_books()
        display_books(books)

    except Exception as e:
        print("Error:", e)


def update_stock_menu():
    print("\n===== UPDATE STOCK =====")

    try:
        book_id = int(input("Enter book ID: "))
        quantity = int(input("Enter quantity to add: "))

        result = library.update_stock(
            book_id,
            quantity
        )

        if result:
            print("Stock updated successfully.")
        else:
            print("Book not found.")

    except ValueError:
        print("Please enter valid numbers.")

    except Exception as e:
        print("Error:", e)


def add_member_menu():
    print("\n===== ADD MEMBER =====")

    name = input("Enter name: ")
    email = input("Enter email: ")
    member_type = input("Enter member type: ")
    status = input("Enter status: ")

    try:
        library.add_member(
            name,
            email,
            member_type,
            status
        )

        print("Member added successfully.")

    except Exception as e:
        print("Error:", e)


def list_members_menu():
    print("\n===== MEMBERS =====")

    try:
        members = library.list_members()
        display_members(members)

    except Exception as e:
        print("Error:", e)


def issue_book_menu():
    print("\n===== ISSUE BOOK =====")

    try:
        book_id = int(input("Enter book ID: "))
        member_id = int(input("Enter member ID: "))

        result = library.issue_book(
            book_id,
            member_id
        )

        print(result)

    except ValueError:
        print("Please enter valid IDs.")

    except Exception as e:
        print("Error:", e)


def return_book_menu():
    print("\n===== RETURN BOOK =====")

    try:
        transaction_id = int(
            input("Enter transaction ID: ")
        )

        result = library.return_book(
            transaction_id
        )

        print(result)

    except ValueError:
        print("Please enter a valid transaction ID.")

    except Exception as e:
        print("Error:", e)


def borrow_history_menu():
    print("\n===== BORROW HISTORY =====")

    try:
        history = library.borrow_history()

        if not history:
            print("No borrow history found.")
            return

        for row in history:
            print(
                f"Transaction ID: {row[0]} | "
                f"Member: {row[1]} | "
                f"Book: {row[2]} | "
                f"Issue Date: {row[3]} | "
                f"Return Date: {row[4]} | "
                f"Status: {row[5]}"
            )

    except Exception as e:
        print("Error:", e)


def top_borrowed_books_menu():
    print("\n===== TOP BORROWED BOOKS =====")

    try:
        books = library.top_borrowed_books()

        if not books:
            print("No borrowing records found.")
            return

        for row in books:
            print(
                f"Book ID: {row[0]} | "
                f"Title: {row[1]} | "
                f"Borrowed: {row[2]} times"
            )

    except Exception as e:
        print("Error:", e)


def delete_book_menu():
    print("\n===== DELETE BOOK =====")

    try:
        book_id = int(
            input("Enter book ID to delete: ")
        )

        result = library.delete_book(book_id)

        if result:
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    except ValueError:
        print("Please enter a valid book ID.")

    except Exception as e:
        print("Error:", e)


def show_menu():

    print("\n")
    print("=" * 40)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Book")
    print("2. Search Book")
    print("3. List Available Books")
    print("4. Update Stock")
    print("5. Add Member")
    print("6. List Members")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. Borrow History")
    print("10. Top Borrowed Books")
    print("11. Delete Book")
    print("0. Exit")

    print("=" * 40)


def main():

    while True:

        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book_menu()

        elif choice == "2":
            search_book_menu()

        elif choice == "3":
            list_available_books_menu()

        elif choice == "4":
            update_stock_menu()

        elif choice == "5":
            add_member_menu()

        elif choice == "6":
            list_members_menu()

        elif choice == "7":
            issue_book_menu()

        elif choice == "8":
            return_book_menu()

        elif choice == "9":
            borrow_history_menu()

        elif choice == "10":
            top_borrowed_books_menu()

        elif choice == "11":
            delete_book_menu()

        elif choice == "0":
            print("Thank you for using Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()