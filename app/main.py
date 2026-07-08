#Day 1[Creating Book Attribute]

import book
import members
import library

print("\n===== Library Details =====")
print("Library Name:", library.library_name)
print("Total Books:", library.total_books)
print("Available Books:", library.total_books - book.available_copies)

print("\n===== Book Details =====")
print("Book ID:", book.book_id)
print("Title:", book.book_title)
print("Author:", book.book_author)
print("Available Books:", book.total_copies - book.available_copies)
if book.available_copies > 0:
    print("Status: Available")
else:
    print("Status: Not Available")

print("\n===== Member Details =====")
print("Member ID:", members.member_id)
print("Member Name:", members.member_name)

# Run using the command: [ python main.py ] in termina