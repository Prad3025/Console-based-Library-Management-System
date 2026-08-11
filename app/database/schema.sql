CREATE DATABASE IF NOT EXISTS library_management;

USE library_management;


CREATE TABLE IF NOT EXISTS books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    copies_available INT NOT NULL DEFAULT 0,
    created_date DATE NOT NULL
);


CREATE TABLE IF NOT EXISTS members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    member_type VARCHAR(50) NOT NULL,
    status VARCHAR(30) NOT NULL
);


CREATE TABLE IF NOT EXISTS issue_transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    issue_date DATE NOT NULL,
    return_date DATE,
    status VARCHAR(30) NOT NULL,

    FOREIGN KEY (book_id)
        REFERENCES books(book_id),

    FOREIGN KEY (member_id)
        REFERENCES members(member_id)
);