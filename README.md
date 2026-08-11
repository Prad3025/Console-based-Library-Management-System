# Library Management System

## Overview

The Library Management System is a console-based application developed using **Python (Object-Oriented Programming)** with **JSON** for data storage. The project also includes a **MySQL database design** to demonstrate database concepts and SQL queries for library management.

---

## Features

### Book Management

* Add a new book
* View all books
* Search books by ID or title
* Delete books
* Issue books
* Return books

### Member Management

* Add a new member
* View all members
* Search members
* Delete members

### Object-Oriented Programming Concepts

* Classes and Objects
* Inheritance
* Encapsulation
* Exception Handling
* File Handling (JSON)

---

## Project Structure

```text
LibraryManagement/
│
├── app/
│   ├── main.py
│   ├── library.py
│   ├── book.py
│   ├── digital_book.py
│   ├── reference_book.py
│   ├── member.py
│   ├── student.py
│   ├── faculty.py
│   ├── issue_transaction.py
│   ├── storage.py
│   ├── exceptions.py
│   ├── books.json
│   └── members.json
│
└── database/
    └── library_management.sql
```

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* JSON
* MySQL
* Git & GitHub

---

## Database Tables

### Users

* user_id
* username
* password
* role

### Books

* book_id
* isbn
* title
* author
* category
* copies_available
* created_date

### Members

* member_id
* name
* email
* member_type
* status

### Issue Transactions

* transaction_id
* book_id
* member_id
* issue_date
* return_date

---

## SQL Operations

The SQL module includes the following operations:

* Add Book
* Update Book Stock
* Search Books
* List Available Books
* Borrow History
* Top Borrowed Books

---

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project directory.

```bash
cd LibraryManagement
```

3. Run the application.

```bash
python main.py
```

4. For the SQL module:

   * Open `database/library_management.sql`
   * Execute the script in MySQL Workbench or another MySQL client.

---

## Future Enhancements

* MySQL integration with Python
* Login and authentication
* Fine calculation for overdue books
* Book reservation system
* GUI using Tkinter or a web interface using Flask/FastAPI

---

## Author

**Pradeep Kumar**

B.Tech Computer Science Engineering (AI & ML)

Christ (Deemed to be University)
