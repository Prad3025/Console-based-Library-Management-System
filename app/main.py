book_ids=[]
book_titles=[]
book_authors=[]
book_status=[]

def addbook():
    print("\n Add Book Details")

    book_id=int(input("enter book Id:"))
    titles=input("enter book title:")
    authors=input("enter book author:")

    book_ids.append(book_id)
    book_titles.append(titles)
    book_authors.append(authors)
    book_status.append("Available")

    print("\n Book Added Successfully")

def view_books():
    if len(book_ids)==0:
        print("\n no books available in the library")
        return
    
    print("\n Book Details")

    for i in range(len(book_ids)):
        print(f"Book ID: {book_ids[i+1]}, Title: {book_titles[i]}, Author: {book_authors[i]}, Status: {book_status[i]}")

def search_books():
    if len(book_ids)==0:
        print("\n no books available in the library")
        return

    search_title=input("Enter book title to search: ")
    found=False

    for i in range(len(book_titles)):
        if book_titles[i].lower()==search_title.lower():
            print(f"\n Book Found: ID: {book_ids[i]}, Title: {book_titles[i]}, Author: {book_authors[i]}, Status: {book_status[i]}")
            found=True
            break

    if not found:
        print(f"\n Book with title '{search_title}' not found.")

def delete_books():
    if len(book_ids)==0:
        print("\n no books available in the Library")
        return
    
    delete_id=int(input("Enter book ID to delete: "))

    found=False

    for i in range(len(book_ids)):
        if book_ids[i]==delete_id:
            book_ids.pop(i)
            book_titles.pop(i)
            book_authors.pop(i)
            book_status.pop(i)

            print(f"\n Book with ID {delete_id} deleted successfully.")
            found=True
            break

def issue_book():
    if len(book_ids)==0:
        print("\n no books available in library")
        return
    
    issue_id=int(input("Enter book ID to issue: "))

    found=False

    for i in range(len(book_ids)):
        if book_ids[i]==issue_id:
            if book_status[i]=="Available":
                book_status[i]="Issued"
                print(f"\n Book with ID {issue_id} issued successfully.")
            else:
                print(f"\n Book with ID {issue_id} is already issued.")
            found=True
            break

        if not found:
            print(f"\n Book with ID {issue_id} not found.")

def return_book():
    if len(book_ids)==0:
        print("\n no book available in library")
        return
    
    return_id=int(input("Enter Book id to return:"))
    found=False

    for i in range(len(book_ids)):
        if book_ids[i]==return_id:
            if book_status[i]=="Issued":
                book_status[i]="Available"
                print(f"\n Book with ID {return_id} returned successfully.")
            else:
                print(f"\n Book with ID {return_id} was not issued.")
            found=True
            break

        if not found:
            print(f"\n Book with ID {return_id} not found.")
        

while True:
    print("\n Library Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        addbook()
    elif choice==2:
        view_books()
    elif choice==3:
        search_books()
    elif choice==4:
        delete_books()
    elif choice==5:
        issue_book()
    elif choice==6:
        return_book()
    elif choice==7:
        print("\n Exiting the program.")
        break
    else:
        print("\n Invalid choice. Please try again.")