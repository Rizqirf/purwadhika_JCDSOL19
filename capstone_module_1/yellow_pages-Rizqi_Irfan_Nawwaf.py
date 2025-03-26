# Yellow Pages App using Python, with CRUD operations
# for Capstone Project  Module 1
# Created by Rizqi Irfan Nawwaf
# Class: JCDSOL-019

"""
Populate Yellow Pages Data
"""
yellow_pages_data = [
    {
        "name": "Rizqi Irfan Nawwaf",
        "phone": "08123456789",
        "address": "Jl. Jendral Sudirman No. 1",
    },
    {
        "name": "John Doe",
        "phone": "08123456788",
        "address": "Jl. Jendral Sudirman No. 2",
    },
    {
        "name": "Jane Doe",
        "phone": "08123456787",
        "address": "Jl. Jendral Sudirman No. 3",
    },
]


"""
Read Function

    Function to show yellow pages data
    Before showing the data, it will calculate the column width dynamically so the shown data will be aligned

    additional feature:
    - show specific contact by index
    - if index is not provided or not an integer, it will show all contacts
"""


def show_yellow_pages(index=None | int):
    print("----------------------------")
    print("Contact List:")

    max_name_length = max(len(contact["name"]) for contact in yellow_pages_data)
    max_phone_length = max(len(contact["phone"]) for contact in yellow_pages_data)
    max_address_length = max(len(contact["address"]) for contact in yellow_pages_data)

    print(
        f"{'index'}\t{'name':<{max_name_length}}\t{'phone':<{max_phone_length}}\t{'address'}"
    )
    if index is not None and type(index) == int:
        contact = yellow_pages_data[index]
        print(
            f"{index}\t{contact["name"]:<{max_name_length}}\t{contact["phone"]:<{max_phone_length}}\t{contact["address"]:<{max_address_length}}"
        )
        print("----------------------------")
        return
    else:
        for i, contact in enumerate(yellow_pages_data):
            print(
                f"{i}\t{contact["name"]:<{max_name_length}}\t{contact["phone"]:<{max_phone_length}}\t{contact["address"]:<{max_address_length}}"
            )
        print("----------------------------")


"""
Additional Feature: Input with Validation
    - Validate name
        * Name can't be empty
        * Name must be alphabetic
        * Name must be less than 50 characters
        * Name must be at least more than 3 characters
    - Validate phone
        * Phone can't be empty
        * Phone number must be numeric
        * Phone number must be less than 15 characters
        * Phone number must be at least 10 characters
        * Phone number must start with 08
    - Validate address
        * Address can't be empty
        * Address must be less than 50 characters
        * Address must be at least more than 10 characters
    - Validate index
        * Index must be in range of yellow_pages_data
        * Index must be an integer
        * Index must be positive
    - Validate confirmation
        * Possitive confirmation must be 'y' or 'Y'
        * Others will be considered as negative confirmation
"""


def name_input():
    def is_valid(name: str):
        if not name:
            print("Name can't be empty")
            return False
        elif not name.replace(" ", "").isalpha():
            print("Name must be alphabetic")
            return False
        elif len(name) > 30:
            print("Name must be less than 50 characters")
            return False
        elif len(name) < 3:
            print("Name must be at least more than 3 characters")
            return False
        return True

    while not is_valid(name := input("Enter name: ")):
        pass
    return name


def phone_input():
    def is_valid(phone: str):
        if not phone:
            print("Phone can't be empty")
            return False
        elif not phone.isdigit():
            print("Phone number must be numeric")
            return False
        elif len(phone) > 15:
            print("Phone number must be less than 15 characters")
            return False
        elif len(phone) < 10:
            print("Phone number must be at least 10 characters")
            return False
        elif not phone.startswith("08"):
            print("Phone number must start with 08")
            return False
        return True

    while not is_valid(phone := input("Enter phone: ")):
        pass
    return phone


def address_input():
    def is_valid(address: str):
        if not address:
            print("Address can't be empty")
            return False
        elif len(address) > 50:
            print("Address must be less than 50 characters")
            return False
        elif len(address) < 10:
            print("Address must be at least more than 10 characters")
            return False
        return True

    while not is_valid(address := input("Enter address: ")):
        pass
    return address


def index_input():
    def is_valid(index: str):
        if not index.isdigit():
            print("Index must be an integer")
            return False
        elif (index := int(index)) < 0 or index >= len(yellow_pages_data):
            print("Index must be in range of yellow_pages_data")
            return False
        return True

    while not is_valid(index := input("Enter index: ")):
        pass

    return int(index)


def confirmation_input(feature: str):
    confirmation = input(f"Are you sure you want to {feature} this contact? (y/n): ")
    if confirmation.lower() != "y":
        return False
    return True


"""
Create Function
    - Add new contact to yellow pages data
    - Validate input
"""


def add_yellow_pages():
    print("----------------------------")
    print("Add New Contact:")

    name = name_input()
    phone = phone_input()
    address = address_input()

    yellow_pages_data.append({"name": name, "phone": phone, "address": address})
    print("----------------------------")
    print("Contact added successfully!")
    print("----------------------------")


"""
Update Function
    - Update existing contact in yellow pages data
    - Validate inputted index
    - Add confirmation before updating
    - Validate input
"""


def update_yellow_pages():
    show_yellow_pages()
    print("----------------------------")

    index = index_input()
    show_yellow_pages(index)

    if not confirmation_input("update"):
        return

    name = name_input()
    phone = phone_input()
    address = address_input()

    yellow_pages_data[index] = {"name": name, "phone": phone, "address": address}
    print("----------------------------")
    print("Contact updated successfully!")
    print("----------------------------")


"""
Delete Function
    - Delete existing contact in yellow pages data
    - Validate inputted index
    - Add confirmation before deleting
"""


def delete_yellow_pages():
    show_yellow_pages()
    print("----------------------------")

    index = index_input()
    show_yellow_pages(index)

    if not confirmation_input("delete"):
        return
    yellow_pages_data.pop(index)
    print("----------------------------")
    print("Contact deleted successfully!")
    print("----------------------------")


"""
Display Menu
    - Show menu
        * Show yellow pages
        * Add contact
        * Update contact
        * Delete contact
        * Exit
    - Main menu
        * Loop until user choose to exit
        * Validate user input(make sure it's an integer before casting)
        * Show menu after each operation
"""


def show_menu():
    print("----------------------------")
    print("Menu:")
    print("1. Show Yellow Pages")
    print("2. Add Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("----------------------------")


def main_menu():
    print("Welcome to Yellow Pages App")
    show_menu()
    while True:
        choice = input("Enter choice: ")
        if not choice.isdigit():
            print("Invalid choice, please try again")
            continue
        else:
            choice = int(choice)

        if choice == 1:
            show_yellow_pages()
        elif choice == 2:
            add_yellow_pages()
        elif choice == 3:
            update_yellow_pages()
        elif choice == 4:
            delete_yellow_pages()
        elif choice == 5:
            print("Thank you for using Yellow Pages App")
            break
        else:
            print("Invalid choice, please try again")

        show_menu()


main_menu()
