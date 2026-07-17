import json

# Custom Exception
class BookNotFound(Exception):
    pass


# Load Books from JSON
try:
    with open("books.json", "r") as file:
        books = json.load(file)
except FileNotFoundError:
    books = []

# Load Members from JSON
try:
    with open("members.json", "r") as file:
        members = json.load(file)
except FileNotFoundError:
    members = []


# Save Books
def save_books():
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)




#members
def save_members():
    with open("members.json","w")as file:
        json.dump(members,file,indent=4)

# Add Member
def add_member():
    try:
        member_id=int(input("Enter Member ID:"))
    except ValueError:
        print("Member ID must be integer")
        return

    for member in members:
        if member['member_id']==member_id:
            print("Member ID Already Exists")
            return
        
    name=input("Enter Member Name:")

    members.append({
        'member_id':member_id,
        'name':name
    })

    save_members()
    print("Member added successfully")

def view_members():
    if not members:
        print('No Member Found')
        return
    
    for member in members:
        print(f'{member["member_id"]} - {member["name"]}')
# Main Menu
while True:

    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Add Member")
    print("8. View Members")
    print("9. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book()

        elif choice == 2:
            view_books()

        elif choice == 3:
            search_book()

        elif choice == 4:
            delete_book()

        elif choice == 5:
            issue_book()

        elif choice == 6:
            return_book()

        elif choice == 7:
            add_member()

        elif choice == 8:
            view_members()

        elif choice == 9:
            print("\nThank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

    except ValueError:
        print("Please enter numbers only.")