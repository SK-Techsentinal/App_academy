contacts = []


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"{name} added successfully.\n")


def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def delete_contact(name):
    match = search_contact(name)
    if match:
        contacts.remove(match)
        print(f"{name} deleted.\n")
    else:
        print(f"No contact found named '{name}'.\n")


def view_all():
    if not contacts:
        print("No contacts saved yet.\n")
        return
    print(f"\n{'--- Contact Book ---':^40}")
    for c in contacts:
        print(f"Name: {c['name']} | Phone: {c['phone']} | Email: {c['email']}")
    print()


def main():
    while True:
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            name = input("Enter name to search: ")
            result = search_contact(name)
            if result:
                print(f"Found: {result}\n")
            else:
                print("Contact not found.\n")
        elif choice == "3":
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == "4":
            view_all()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.\n")


if __name__ == "__main__":
    main()
