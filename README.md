# 📚 Console-Based Library Management System

A Python-based **console application for managing library operations** using Object-Oriented Programming (OOP). The project supports book and member management, book issuing and returns, inventory tracking, borrowing history, and reporting through a simple command-line interface.

The repository also includes a separate **MySQL database layer** with a schema and SQL queries for practicing relational database design and SQL operations.

## ✨ Features

### 📖 Book Management
- Add a new book
- Search books by title, author, or ISBN
- List available books
- Update book stock
- Delete books

### 👤 Member Management
- Add library members
- List members
- Store member type and status

### 🔄 Library Transactions
- Issue books to members
- Return issued books
- Track borrowing history
- View top borrowed books

### 🧱 Object-Oriented Design
The application is structured using Python classes and demonstrates:
- Classes and objects
- Inheritance
- Encapsulation
- Exception handling
- Modular code organization

### 🗄️ Database Layer
The repository includes a MySQL implementation containing:
- Database connection handling
- SQL schema
- Reusable SQL queries
- Inventory and borrowing-related operations

## 🛠️ Technologies Used

- **Python 3**
- **Object-Oriented Programming (OOP)**
- **MySQL**
- **SQL**
- **JSON / File-based persistence concepts**
- **Git & GitHub**

## 📂 Project Structure

```text
Console-based-Library-Management-System/
│
├── app/
│   ├── main.py
│   ├── exceptions.py
│   ├── utils.py
│   │
│   ├── models/
│   │   ├── book.py
│   │   ├── digital_book.py
│   │   ├── reference_book.py
│   │   ├── member.py
│   │   ├── student.py
│   │   ├── faculty.py
│   │   ├── library.py
│   │   ├── transactions.py
│   │   └── converters.py
│   │
│   └── database/
│       ├── connection.py
│       ├── queries.py
│       ├── schema.sql
│       ├── requirements.txt
│       └── __init__.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Make sure you have:

- Python 3.x installed
- MySQL installed and running if you want to use the database module
- Git installed

### 1. Clone the repository

```bash
git clone https://github.com/Prad3025/Console-based-Library-Management-System.git
```

### 2. Move into the project directory

```bash
cd Console-based-Library-Management-System
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

For the database module, install its dependencies as well:

```bash
pip install -r app/database/requirements.txt
```

### 4. Run the console application

From the project root:

```bash
python app/main.py
```

## 🖥️ Available Console Operations

The application provides a menu-driven interface with options such as:

```text
1. Add Book
2. Search Book
3. List Available Books
4. Update Stock
5. Add Member
6. List Members
7. Issue Book
8. Return Book
9. Borrow History
10. Top Borrowed Books
11. Delete Book
0. Exit
```

## 🗃️ Database Setup

The MySQL database files are located in `app/database/`.

### Create the database schema

Open `app/database/schema.sql` in MySQL Workbench or another MySQL client and execute the script.

The database layer contains code for:

- Connecting to MySQL
- Managing books and stock
- Searching and listing books
- Recording borrowing activity
- Viewing borrowing history
- Finding frequently borrowed books

> Configure your MySQL connection settings in the database connection module before running database-related functionality.

## 🎯 Project Objectives

This project was built to practice and demonstrate:

- Python OOP principles
- Inheritance and class relationships
- Modular application design
- Exception handling
- Input validation
- Library inventory management
- Transaction management
- SQL and relational database concepts
- Git version control

## 🔮 Future Improvements

- Add user authentication and role-based access
- Integrate the Python application directly with MySQL
- Add overdue fine calculation
- Implement book reservation functionality
- Add detailed reports and dashboards
- Build a GUI using Tkinter or a web interface using Flask/FastAPI

## 👨‍💻 Author

**Pradeep Kumar**  
B.Tech Computer Science Engineering (AI & ML)  
Christ (Deemed to be University)

## 📌 Repository

[GitHub Repository](https://github.com/Prad3025/Console-based-Library-Management-System)

---

⭐ If you find this project useful, consider giving the repository a star!
