from storage import load_books, save_books, load_members, save_members
from exceptions import BookNotFound, MemberNotFound


class Library:

    def __init__(self):
        self.books = load_books()
        self.members = load_members()

    # ---------------- BOOK METHODS ---------------- #

    def add_book(self):

        print("\n----- Add Book -----")

        try:
            book_id = int(input("Enter Book ID: "))
        except ValueError:
            print("Book ID must be a number.")
            return

        for book in self.books:
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

        self.books.append(book)
        save_books(self.books)

        print("Book added successfully!")

    def view_books(self):

        if not self.books:
            print("\nNo books available.")
            return

        print("\n========== Book Details ==========")

        for book in sorted(self.books, key=lambda x: x["title"]):

            print(f"""
Book ID : {book["book_id"]}
Title   : {book["title"]}
Author  : {book["author"]}
Status  : {book["status"]}
""")

    def search_book(self):

        if not self.books:
            print("\nNo books available.")
            return

        search = input("Enter Book Title or Book ID: ")

        try:

            for book in self.books:

                if (
                    str(book["book_id"]) == search or
                    book["title"].lower() == search.lower()
                ):

                    print("\nBook Found")

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

    def delete_book(self):

        if not self.books:
            print("\nNo books available.")
            return

        try:

            delete_id = int(input("Enter Book ID to Delete: "))

            for book in self.books:

                if book["book_id"] == delete_id:

                    self.books.remove(book)
                    save_books(self.books)

                    print("Book deleted successfully!")
                    return

            raise BookNotFound("Book ID not found.")

        except ValueError:
            print("Please enter a valid number.")

        except BookNotFound as e:
            print(e)

    def issue_book(self):

        if not self.books:
            print("\nNo books available.")
            return

        try:

            issue_id = int(input("Enter Book ID to Issue: "))

            for book in self.books:

                if book["book_id"] == issue_id:

                    if book["status"] == "Available":
                        book["status"] = "Issued"
                        save_books(self.books)
                        print("Book issued successfully!")

                    else:
                        print("Book is already issued.")

                    return

            raise BookNotFound("Book ID not found.")

        except ValueError:
            print("Please enter a valid number.")

        except BookNotFound as e:
            print(e)

    def return_book(self):

        if not self.books:
            print("\nNo books available.")
            return

        try:

            return_id = int(input("Enter Book ID to Return: "))

            for book in self.books:

                if book["book_id"] == return_id:

                    if book["status"] == "Issued":
                        book["status"] = "Available"
                        save_books(self.books)
                        print("Book returned successfully!")

                    else:
                        print("Book is already available.")

                    return

            raise BookNotFound("Book ID not found.")

        except ValueError:
            print("Please enter a valid number.")

        except BookNotFound as e:
            print(e)

    # ---------------- MEMBER METHODS ---------------- #

    def add_member(self):

        print("\n----- Add Member -----")

        try:
            member_id = int(input("Enter Member ID: "))
        except ValueError:
            print("Member ID must be a number.")
            return

        for member in self.members:
            if member["member_id"] == member_id:
                print("Member ID already exists.")
                return

        name = input("Enter Member Name: ")

        member = {
            "member_id": member_id,
            "name": name
        }

        self.members.append(member)
        save_members(self.members)

        print("Member added successfully!")

    def view_members(self):

        if not self.members:
            print("\nNo members available.")
            return

        print("\n========== Member Details ==========")

        for member in self.members:

            print(f"""
Member ID : {member["member_id"]}
Name      : {member["name"]}
""")

    def search_member(self):

        if not self.members:
            print("\nNo members available.")
            return

        search = input("Enter Member ID or Member Name: ")

        try:

            for member in self.members:

                if (
                    str(member["member_id"]) == search or
                    member["name"].lower() == search.lower()
                ):

                    print("\nMember Found")

                    print(f"""
Member ID : {member["member_id"]}
Name      : {member["name"]}
""")
                    return

            raise MemberNotFound("Member not found.")

        except MemberNotFound as e:
            print(e)

    def delete_member(self):

        if not self.members:
            print("\nNo members available.")
            return

        try:

            delete_id = int(input("Enter Member ID to Delete: "))

            for member in self.members:

                if member["member_id"] == delete_id:

                    self.members.remove(member)
                    save_members(self.members)

                    print("Member deleted successfully!")
                    return

            raise MemberNotFound("Member ID not found.")

        except ValueError:
            print("Please enter a valid number.")

        except MemberNotFound as e:
            print(e)