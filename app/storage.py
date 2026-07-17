import json

def load_books():
    try:
        with open("books.json","r")as file:
            return json.load(file)
        
    except (FileNotFoundError,json.JSONDecodeError):
        return []
    
def save_books(books):
    with open('books.json','w')as file:
        json.dump(books,file,indent=4)

def load_members():
    try:
        with open('members.json','r') as file:
            return json.load(file)
        
    except (FileNotFoundError,json.JSONDecodeError):
        return []
    
def save_members(members):
    with open('members.json','w') as file:
        json.dump(members,file,indent=4)