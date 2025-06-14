import sys

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add(self):
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email (optional): ").strip()
        address = input("Address (optional): ").strip()
        self.contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        print("✅ Contact added!\n")

    def show_all(self, contacts_to_show=None):
        entries = contacts_to_show if contacts_to_show is not None else self.contacts
        if not entries:
            print("⚠ No contacts available.\n")
            return
        for i, person in enumerate(entries, 1):
            print(f"{i}. {person['name']} | {person['phone']}")
            if person['email']:
                print(f"   Email: {person['email']}")
            if person['address']:
                print(f"   Address: {person['address']}")
        print()

    def search(self):
        keyword = input("Search by name or phone: ").strip().lower()
        results = [p for p in self.contacts if keyword in p['name'].lower() or keyword in p['phone']]
        self.show_all(results)

    def edit(self):
        self.show_all()
        try:
            index = int(input("Select contact number to edit: ")) - 1
            if not (0 <= index < len(self.contacts)):
                print("❗ Invalid number.\n")
                return
            person = self.contacts[index]
            print("Press Enter to keep existing value.")
            new_name = input(f"Name [{person['name']}]: ").strip() or person['name']
            new_phone = input(f"Phone [{person['phone']}]: ").strip() or person['phone']
            new_email = input(f"Email [{person['email']}]: ").strip() or person['email']
            new_address = input(f"Address [{person['address']}]: ").strip() or person['address']
            self.contacts[index] = {
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            }
            print("✅ Contact updated!\n")
        except ValueError:
            print("❗ Please enter a valid number.\n")

    def remove(self):
        self.show_all()
        try:
            index = int(input("Select contact number to remove: ")) - 1
            if not (0 <= index < len(self.contacts)):
                print("❗ Invalid number.\n")
                return
            del self.contacts[index]
            print("✅ Contact removed!\n")
        except ValueError:
            print("❗ Please enter a valid number.\n")

    def run(self):
        while True:
            print("📒 Contact Book")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Edit Contact")
            print("5. Remove Contact")
            print("6. Exit")
            option = input("Choose an option: ").strip()
            if option == "1":
                self.add()
            elif option == "2":
                self.show_all()
            elif option == "3":
                self.search()
            elif option == "4":
                self.edit()
            elif option == "5":
                self.remove()
            elif option == "6":
                print("👋 Goodbye!")
                sys.exit()
            else:
                print("❗ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    app = ContactBook()
    app.run()