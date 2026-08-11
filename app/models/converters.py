from models.book import Book
from models.member import Member
from models.transactions import IssueTransaction


def book_from_row(row):
    return Book(
        book_id=row[0],
        isbn=row[1],
        title=row[2],
        author=row[3],
        category=row[4],
        copies_available=row[5],
        created_date=row[6]
    )


def member_from_row(row):
    return Member(
        member_id=row[0],
        name=row[1],
        email=row[2],
        member_type=row[3],
        status=row[4]
    )


def transaction_from_row(row):
    return IssueTransaction(
        transaction_id=row[0],
        book_id=row[1],
        member_id=row[2],
        issue_date=row[3],
        return_date=row[4],
        status=row[5]
    )