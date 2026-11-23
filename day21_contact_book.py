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