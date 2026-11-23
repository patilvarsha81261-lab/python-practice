#day21_contact_book.py (easy version)

contacts = {}

while True:
    print("\n1. Add contact")
    print("2. Show contacts")
    print("3. Search")
    print("4. Quit")
    choice = input("Choose (1-4): ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Saved")

    elif choice == "2":
        for name in contacts:
            print(name, "-", contacts[name])

    elif choice == "3":
        search = input("Name to find: ")
        if search in contacts:
            print(search, "-", contacts[search])
        else:
            print("Not found")

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Please choose 1 to 4")



        #Full version (class, saved file, checks, update and delete)


# day21_contact_book.py
import json
import re

FILENAME = "contacts.json"


def clean_phone(phone):
    return re.sub(r"[ -]", "", phone)


def valid_phone(phone):
    return re.fullmatch(r"\+?\d{10,13}", phone) is not None


def valid_email(email):
    return email == "" or re.fullmatch(r"[\w.+-]+@[\w-]+\.[\w.]+", email) is not None


class ContactBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load()

    def load(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.contacts, f, indent=2)

    def find(self, name):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                return contact
        return None

    def add(self, name, phone, email):
        if self.find(name):
            raise ValueError("A contact with that name already exists")
        self.contacts.append({"name": name, "phone": phone, "email": email})
        self.contacts.sort(key=lambda c: c["name"].lower())
        self.save()

    def search(self, text):
        text = text.lower()
        return [c for c in self.contacts
                if text in c["name"].lower() or text in c["phone"]]

    def update(self, name, phone, email):
        contact = self.find(name)
        if contact is None:
            raise ValueError("Contact not found")
        if phone:
            contact["phone"] = phone
        if email:
            contact["email"] = email
        self.save()

    def delete(self, name):
        contact = self.find(name)
        if contact is None:
            raise ValueError("Contact not found")
        self.contacts.remove(contact)
        self.save()


def show(contacts):
    if len(contacts) == 0:
        print("No contacts found")
        return
    print(f"\n{'Name':<20}{'Phone':<16}{'Email'}")
    for c in contacts:
        print(f"{c['name']:<20}{c['phone']:<16}{c['email']}")


def ask_phone(required=True):
    while True:
        phone = clean_phone(input("Phone (10-13 digits): ").strip())
        if phone == "" and not required:
            return ""
        if valid_phone(phone):
            return phone
        print("Please type a valid phone number, digits only")


def ask_email():
    while True:
        email = input("Email (optional): ").strip()
        if valid_email(email):
            return email
        print("That email doesn't look right")


book = ContactBook(FILENAME)

while True:
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. Show all contacts")
    print("3. Search")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Quit")
    choice = input("Choose (1-6): ")

    try:
        if choice == "1":
            name = input("Name: ").strip()
            if name == "":
                print("Name cannot be empty")
                continue
            phone = ask_phone()
            email = ask_email()
            book.add(name, phone, email)
            print("Contact added")

        elif choice == "2":
            show(book.contacts)

        elif choice == "3":
            text = input("Search by name or phone: ").strip()
            show(book.search(text))

        elif choice == "4":
            name = input("Name of the contact to update: ").strip()
            if book.find(name) is None:
                print("Contact not found")
                continue
            print("Leave a field empty to keep the old value")
            phone = ask_phone(required=False)
            email = ask_email()
            book.update(name, phone, email)
            print("Contact updated")

        elif choice == "5":
            name = input("Name of the contact to delete: ").strip()
            if input(f"Delete {name}? (y/n): ").lower() == "y":
                book.delete(name)
                print("Contact deleted")

        elif choice == "6":
            print("Bye! Day 21 done.")
            break

        else:
            print("Please choose 1 to 6")

    except ValueError as error:
        print("Error:", error)