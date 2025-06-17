import json

try:
    with open("phonebook.json", "r") as file:
        contacts = json.load(file)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    contacts = {}

def save_contacts():
    with open("phonebook.json", "w") as file:
        json.dump(contacts, file, indent = 4)

def add_person():
    name = input("What is the name of the person you would like to add: ")
    if name.lower() == "quit":
        return False

    number = input("What is the phone number of the person you would like to add: ")
    if number.lower() == "quit":
        return False
    elif not number.isdigit():
        print("Please enter only numbers for the phone.")
        return True
    elif len(number) != 10:
        print("The phone number must be 10 digits long.")
        return True

    contacts[name] = number
    save_contacts()
    return True

def remove_person():
    name = input("What person would you like to delete from your contact list?: ")
    if name.lower() == "quit":
        return False

    if name in contacts:
        del contacts[name]
        print(f"{name} removed")
        save_contacts()
    else:
        print(f"{name} not found.")
    return True


def edit_person():

    name = input("What contact would you like to edit?: ")
    if name.lower() == "quit":
        return False
    if name not in contacts:
        print("Contact not found")
        return True
    
    print("1. Change name")
    print("2. Change phone number")
    choice = input("Choose an option: ").strip().lower()

    if choice in ("1", "change name"):
        new_name = input("What name would you like to change to?: ")
        if new_name in contacts:
            print("That contact already exists")
            return True
        contacts[new_name] = contacts[name]
        del contacts[name] 
        save_contacts()
    elif choice in ("2", "change phone number"):
        new_phone = input("Enter new phone number: ")
        if not new_phone.isdigit() or len(new_phone) != 10:
            print("Phone number must be exactly 10 digits.")
            return True
        contacts[name] = new_phone
        save_contacts()
    else:
        print("Invalid choice.")
    return True


def phone_book():
    print(f"\nYour phone book:")
    print("-" * 20)

    if contacts:
        for name, number in contacts.items():
            print(f"{name:<10}: {number}")
    else: 
        print("Phone book is empty.")
    
    print("-" * 20)
    return True


while True:
    print("1. Add a person")
    print("2. Remove a person")
    print("3. View phone book")
    print("4. Update contact")
    print("5. Quit")
    choice = input()
    choice = choice.strip().lower()
    if choice in ("1", "add a person"):
        add_person()
        
    elif choice in ("2", "remove a person"):
        remove_person()
        
    elif choice in ("3", "view phone book"):
        phone_book()
        print("\n")
    elif choice in ("4", "update contact"):
        edit_person()
    elif choice in ("5", "quit"):
        print("Saving contacts and quitting...")
        save_contacts()
        break
    else:
        print("Invalid choice. Please try again.")