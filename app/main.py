from books import (
    add_book,
    view_books,
    search_book,
    delete_book,
    issue_book,
    return_book
)

from members import (
    add_member,
    view_members,
    search_member,
    delete_member
)

while True:

    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Add Member")
    print("8. View Members")
    print("9. Search Member")
    print("10. Delete Member")
    print("11. Exit")

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
            add_member()

        elif choice == 8:
            view_members()

        elif choice == 9:
            search_member()

        elif choice == 10:
            delete_member()

        elif choice == 11:
            print("\nThank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 11.")

    except ValueError:
        print("Please enter numbers only.")