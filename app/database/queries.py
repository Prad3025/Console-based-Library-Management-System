from connection import get_connection
from datetime import date


# =========================
# BOOK OPERATIONS
# =========================

def add_book(isbn, title, author, category, copies_available, created_date):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        INSERT INTO books
        (isbn, title, author, category, copies_available, created_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            isbn,
            title,
            author,
            category,
            copies_available,
            created_date
        )

        cursor.execute(query, values)
        connection.commit()

        return True

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()


def update_stock(book_id, quantity):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        UPDATE books
        SET copies_available = copies_available + %s
        WHERE book_id = %s
        """

        cursor.execute(query, (quantity, book_id))

        if cursor.rowcount == 0:
            connection.rollback()
            return False

        connection.commit()
        return True

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()


def search_books(keyword):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        SELECT *
        FROM books
        WHERE title LIKE %s
           OR author LIKE %s
           OR isbn LIKE %s
        """

        search_value = f"%{keyword}%"

        cursor.execute(
            query,
            (search_value, search_value, search_value)
        )

        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


def list_available_books():

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        SELECT *
        FROM books
        WHERE copies_available > 0
        """

        cursor.execute(query)

        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


def delete_book(book_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        DELETE FROM books
        WHERE book_id = %s
        """

        cursor.execute(query, (book_id,))

        if cursor.rowcount == 0:
            connection.rollback()
            return False

        connection.commit()
        return True

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()


# =========================
# MEMBER OPERATIONS
# =========================

def add_member(name, email, member_type, status):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        INSERT INTO members
        (name, email, member_type, status)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            name,
            email,
            member_type,
            status
        )

        cursor.execute(query, values)
        connection.commit()

        return True

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()


def list_members():

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        SELECT *
        FROM members
        """

        cursor.execute(query)

        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


# =========================
# ISSUE BOOK
# =========================

def issue_book(book_id, member_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Check book
        query = """
        SELECT copies_available
        FROM books
        WHERE book_id = %s
        """

        cursor.execute(query, (book_id,))

        book = cursor.fetchone()

        if book is None:
            return "Book not found"

        if book[0] <= 0:
            return "Book is not available"

        # Check member
        query = """
        SELECT status
        FROM members
        WHERE member_id = %s
        """

        cursor.execute(query, (member_id,))

        member = cursor.fetchone()

        if member is None:
            return "Member not found"

        if member[0] != "Active":
            return "Member is not active"

        # Reduce book copies
        query = """
        UPDATE books
        SET copies_available = copies_available - 1
        WHERE book_id = %s
        """

        cursor.execute(query, (book_id,))

        # Create transaction
        query = """
        INSERT INTO issue_transactions
        (book_id, member_id, issue_date, status)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            book_id,
            member_id,
            date.today(),
            "Issued"
        )

        cursor.execute(query, values)

        connection.commit()

        return "Book issued successfully"

    except Exception:

        connection.rollback()

        raise

    finally:

        cursor.close()
        connection.close()


# =========================
# RETURN BOOK
# =========================

def return_book(transaction_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Find transaction
        query = """
        SELECT book_id, status
        FROM issue_transactions
        WHERE transaction_id = %s
        """

        cursor.execute(query, (transaction_id,))

        transaction = cursor.fetchone()

        if transaction is None:
            return "Transaction not found"

        book_id = transaction[0]
        status = transaction[1]

        if status == "Returned":
            return "Book has already been returned"

        # Increase book copies
        query = """
        UPDATE books
        SET copies_available = copies_available + 1
        WHERE book_id = %s
        """

        cursor.execute(query, (book_id,))

        # Update transaction
        query = """
        UPDATE issue_transactions
        SET return_date = %s,
            status = %s
        WHERE transaction_id = %s
        """

        values = (
            date.today(),
            "Returned",
            transaction_id
        )

        cursor.execute(query, values)

        connection.commit()

        return "Book returned successfully"

    except Exception:

        connection.rollback()

        raise

    finally:

        cursor.close()
        connection.close()


# =========================
# BORROW HISTORY
# =========================

def borrow_history():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        query = """
        SELECT
            issue_transactions.transaction_id,
            members.name,
            books.title,
            issue_transactions.issue_date,
            issue_transactions.return_date,
            issue_transactions.status

        FROM issue_transactions

        JOIN books
            ON issue_transactions.book_id = books.book_id

        JOIN members
            ON issue_transactions.member_id = members.member_id

        ORDER BY issue_transactions.issue_date DESC
        """

        cursor.execute(query)

        return cursor.fetchall()

    finally:

        cursor.close()
        connection.close()


# =========================
# TOP BORROWED BOOKS
# =========================

def top_borrowed_books():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        query = """
        SELECT
            books.book_id,
            books.title,
            COUNT(issue_transactions.transaction_id)
                AS borrow_count

        FROM issue_transactions

        JOIN books
            ON issue_transactions.book_id = books.book_id

        GROUP BY
            books.book_id,
            books.title

        ORDER BY borrow_count DESC

        LIMIT 5
        """

        cursor.execute(query)

        return cursor.fetchall()

    finally:

        cursor.close()
        connection.close()