from database.queries import (
    add_book,
    update_stock,
    search_books,
    list_available_books,
    delete_book,
    add_member,
    list_members,
    issue_book,
    return_book,
    borrow_history,
    top_borrowed_books
)

from models.converters import (
    book_from_row,
    member_from_row,
    transaction_from_row
)


class Library:

    def add_book(
        self,
        isbn,
        title,
        author,
        category,
        copies_available,
        created_date
    ):
        return add_book(
            isbn,
            title,
            author,
            category,
            copies_available,
            created_date
        )

    def update_stock(self, book_id, quantity):
        return update_stock(book_id, quantity)

    def search_books(self, keyword):

        rows = search_books(keyword)

        return [
            book_from_row(row)
            for row in rows
        ]

    def list_available_books(self):

        rows = list_available_books()

        return [
            book_from_row(row)
            for row in rows
        ]

    def delete_book(self, book_id):
        return delete_book(book_id)

    def add_member(
        self,
        name,
        email,
        member_type,
        status
    ):
        return add_member(
            name,
            email,
            member_type,
            status
        )

    def list_members(self):

        rows = list_members()

        return [
            member_from_row(row)
            for row in rows
        ]

    def issue_book(self, book_id, member_id):
        return issue_book(book_id, member_id)

    def return_book(self, transaction_id):
        return return_book(transaction_id)

    def borrow_history(self):

        rows = borrow_history()

        return rows

    def top_borrowed_books(self):

        rows = top_borrowed_books()

        return rows