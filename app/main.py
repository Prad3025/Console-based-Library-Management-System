from library import Library

library = Library()

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
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            library.add_book()

        elif choice == 2:
            library.view_books()

        elif choice == 3:
            library.search_book()

        elif choice == 4:
            library.delete_book()

        elif choice == 5:
            library.issue_book()

        elif choice == 6:
            library.return_book()

        elif choice == 7:
            library.add_member()

        elif choice == 8:
            library.view_members()

        elif choice == 9:
            library.search_member()

        elif choice == 10:
            library.delete_member()

        elif choice == 11:
            print("\nThank you for using the Library Management System.")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 11.")

    except ValueError:
        print("\nPlease enter numbers only.")