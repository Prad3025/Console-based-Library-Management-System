from storage import save_members, load_members
from exceptions import MemberNotFound

members=load_members()

def add_member():
    print("\n --Add Members--")

    try:
        member_id=int(input("Enter member Id:"))
    except ValueError:
        print("Member Id Must be Number")
        return
    
    for member in members:
        if member['member_id']==member_id:
            print("Member Id Already Exists")
            return
        
    name=input("Enter Member Name: ")

    member={
        'member_id':member_id,
        'name':name
    }

    members.append(member)
    save_members(members)

def view_members():
    if not members:
        print('No Member Found')
        return
    
    for member in members:
        print(f'{member["member_id"]} - {member["name"]}')


def search_member():

    if not members:
        print("\nNo members available.")
        return

    search = input("Enter Member ID or Member Name: ")

    try:
        for member in members:

            if (str(member["member_id"]) == search or
                    member["name"].lower() == search.lower()):

                print("\nMember Found")

                print(f"""
Member ID : {member["member_id"]}
Name      : {member["name"]}
""")
                return

        raise MemberNotFound("Member not found.")

    except MemberNotFound as e:
        print(e)

def delete_member():

    if not members:
        print("\nNo members available.")
        return

    try:
        delete_id = int(input("Enter Member ID to Delete: "))

        for member in members:

            if member["member_id"] == delete_id:

                members.remove(member)
                save_members(members)

                print("Member deleted successfully!")
                return

        raise MemberNotFound("Member ID not found.")

    except ValueError:
        print("Please enter a valid number.")

    except MemberNotFound as e:
        print(e)