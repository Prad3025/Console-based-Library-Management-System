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