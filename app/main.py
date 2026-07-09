book_ids=[]
book_titles=[]
book_authors=[]

while True:
    print('\n======== Library Management System ====')
    print("1.View Books")
    print("2.Add Book")
    print("3.Search Book")
    print("4.Exit")

    choice=int(input("Enter your choice (1-4): "))

    if choice==1:
        if len(book_ids)==0:
            print("No Books Available")
        else:
            print("\n Linst of Books")
            for i in range(len(book_ids)):
                print(f"Book ID:{book_ids[i]}")
                print(f"Book Title:{book_titles[i]}")
                print(f"Book Authors:{book_authors[i]}")

    elif choice==2:
        print("\n Add Book")
        book_id=int(input("Enter book Id:"))
        book_title=input("Enter Book Title:")
        book_author=input("Enter Book Author:")
        book_ids.append(book_id)
        book_titles.append(book_title)
        book_authors.append(book_author)

        print("Book Added Successfully")

    elif choice==3:
        search_id=int(input("Enter Book ID to Search:"))
        if search_id in book_ids:
            index=book_ids.index(search_id)
            print(f"Book Title: {book_titles[index]}")
            print(f"Book Author: {book_authors[index]}")
        else:
            print("Book not found.")

    elif choice==4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")