# 📚 Console-Based Library Management System

A simple **Console-Based Library Management System** developed in **Python**. This project allows users to manage library books through a menu-driven interface and stores data persistently using JSON files.

---

## 🚀 Features

* ➕ Add a new book
* 📖 View all books
* 🔍 Search a book by title
* ❌ Delete a book
* 📤 Issue a book
* 📥 Return a book
* 💾 Persistent storage using `books.json`
* ⚠️ Custom exception handling (`BookNotFound`)
* ✅ Input validation using `try`/`except`

---

## 🛠️ Technologies Used

* Python 3
* JSON (File Handling)
* Exception Handling
* Git & GitHub

---

## 📂 Project Structure

```text
LibraryManagementSystem/
│
├── app/
│   ├── main.py
│   ├── books.json
│   └── members.json
│
├── README.md
└── venv/
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/Prad3025/Console-based-Library-Management-System.git
```

2. Navigate to the project folder:

```bash
cd Console-based-Library-Management-System
```

3. (Optional) Create and activate a virtual environment.

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

4. Run the application:

```bash
python app/main.py
```

---

## 📋 Menu

```text
========== Library Management System ==========
1. Add Book
2. View Books
3. Search Book
4. Delete Book
5. Issue Book
6. Return Book
7. Exit
```

---

## 📁 Data Storage

The application stores data in JSON files:

* `books.json` – Stores book details
* `members.json` – Reserved for member information

All book changes are automatically saved, so data remains available even after closing the application.

---

## ⚠️ Exception Handling

The project includes:

* Custom `BookNotFound` exception
* `FileNotFoundError` handling for JSON files
* `ValueError` handling for invalid numeric input

---

## 🎯 Learning Outcomes

This project demonstrates:

* Python functions
* Lists and dictionaries
* JSON file handling
* Exception handling
* Menu-driven programming
* Git and GitHub version control

---

## 👨‍💻 Author

**Pradeep Kumar**

GitHub: https://github.com/Prad3025
