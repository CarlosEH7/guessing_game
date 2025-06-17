contacts = {}

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
        print("The phone number can only be 8 digits long.")
        return True

    contacts[name] = number

def remove_person():
    name = input("What person would you like to delete from your contact list?: ")
    if name.lower() == "quit":
        return False
    if name in contacts:
        del contacts[name]
        print(f"{name} removed")
    else:
        print(f"{name} not found.")


while True:
    print(f"1.Add a person \n 2.Remove a person \n 3. View phone book \n 4. Quit")
    choice = input()
    if choice == 1 or choice == "Add a person" or choice == "1.Add a person" or choice == "Add":
        add_person()
        break
    elif choice == 2 or choice == "Remove a person" or choice == "2.Remove a person" or choice == "Remove":
        remove_person()
        break
    elif choice == 3 or choice == "View phone book" or choice == "3.View phone book" or choice == "Phone Book":
        break
    elif
    pass

print("Your phone book:")
print("-" * 20)

for name, number in contacts.items():
    print(f"{name:<10}: {number}")
    
print("-" * 20)


    