import json
import os

contacts = []

#Load contacts to file
if os.path.exists("contacts.json"):
    with open("contacts.json", "r") as file:
        contacts = json.load(file)

#Save contacts to file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

#Show menu function
def show_menu():
    print("\n1 - Add new contact")
    print("2 - View all contacts")
    print("3 - Search for contact")
    print("4 - Delete contact")
    print("0 - Exit")

#Validate input function
def get_valid_input(prompt):
    value = input(prompt)
    return value.strip()

#Add a new contact function
def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contacts.append({"name": name, "phone": phone, "email": email})

    save_contacts()
    print("Contact added")

#View all contacts function
def view_contacts():
    if not contacts:
        print("No contacts found")
        return

    for i, contact in enumerate(contacts):
        print(f"{i+1}. {contact['name']} | {contact['phone']} | {contact['email']}")

#Search contact function
def search_contact():
    if not contacts:
        print("No contacts found")
        return

    name = get_valid_input("Name to search: ")
    found = False

    for contact in contacts:
        if name.lower() in contact["name"].lower():
            print(f"{contact['name']} | {contact['phone']} | {contact['email']}")
            found = True

    if not found:
        print("No contacts found")

#Delete contact function
def delete_contact():
    if not contacts:
        print("No contacts found")
        return

    name = get_valid_input("Name to delete: ")
    found = False
    for i, contact in enumerate(contacts):
        if name.lower() in contact["name"].lower():
            confirm = input(f"Delete {contact['name']}? y/n: ").lower()

            if confirm == "y":
                contacts.pop(i)
                save_contacts()
                print("Contact deleted")
            else:
                print("Cancelled")

            found = True
            break

    if not found:
        print("No contacts found")

#Main loop
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if not choice.isdigit():
        print("Invalid choice")
        continue

    choice = int(choice)

    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        delete_contact()
    elif choice == 0:
        print("Good Bye")
        break
    else:
        print("Invalid choice")