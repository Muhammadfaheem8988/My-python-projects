def add_contact(contacts):
    """Adds a new contact to the dictionary."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print(f"Contact '{name}' added.")

def view_contacts(contacts):
    """Displays all saved contacts."""
    if not contacts:
        print("\nContact book is empty.")
        return
    print("\n--- Contacts ---")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    print("----------------")

def search_contact(contacts):
    """Searches for a specific contact."""
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"Found: {name} - {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    """Deletes a specific contact from the dictionary."""
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Error: Contact '{name}' not found.")
        

def main():
    """Main entry point for Contact Book."""
    contacts = {}
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()