class PhoneBook:
    def __init__(self):
        self.__contacts: dict[str, dict[str, str | int]] = {}

    def __create_contact(self) -> None:
        name = input("Enter the name: ").strip().lower()
        if name in self.__contacts:
            print(f"Contact '{name}' already exists!")
        else:
            try:
                age = int(input("Enter your age: ").strip())
                email = input("Enter your email ID: ").strip()
                phone = input("Enter your phone number: ").strip()
                self.__contacts[name] = {"age": age, "email": email, "phone": phone}
                print(f"Contact '{name}' created successfully.")
            except ValueError:
                print("Invalid input! Age must be an integer.")

    def __view_contact(self) -> None:
        name = input("Enter the contact name to view: ").strip().lower()
        if name not in self.__contacts:
            print(f"Contact '{name}' not found.")
        else:
            contact = self.__contacts[name]
            print(f"Details of contact '{name}':")
            for key, value in contact.items():
                print(f"  {key.capitalize()}: {value}")

    def __update_contact(self) -> None:
        name = input("Enter the name to update contact: ").strip().lower()
        if name not in self.__contacts:
            print(f"Contact '{name}' not found.")
        else:
            try:
                age = int(input("Enter your age: ").strip())
                email = input("Enter your email ID: ").strip()
                phone = input("Enter your phone number: ").strip()
                self.__contacts[name] = {"age": age, "email": email, "phone": phone}
                print(f"Contact '{name}' updated successfully.")
            except ValueError:
                print("Invalid input! Age must be an integer.")

    def __delete_contact(self) -> None:
        name = input("Enter the contact name to delete: ").strip().lower()
        if name not in self.__contacts:
            print(f"Contact '{name}' not found.")
        else:
            del self.__contacts[name]
            print(f"Contact '{name}' deleted successfully.")

    def __count_total_contacts(self) -> None:
        total_contacts = len(self.__contacts)
        if total_contacts == 0:
            print("The phonebook is empty.")
        else:
            print(f"The total number of contacts is: {total_contacts}")

    def __search_contact(self) -> None:
        name = input("Enter the contact name to search: ").strip().lower()
        if name not in self.__contacts:
            print(f"Contact '{name}' not found.")
        else:
            contact = self.__contacts[name]
            print(f"Details of contact '{name}':")
            for key, value in contact.items():
                print(f"  {key.capitalize()}: {value}")

    @staticmethod
    def run_script() -> None:
        self: PhoneBook = PhoneBook()
        options = {
            1: self.__create_contact,
            2: self.__view_contact,
            3: self.__update_contact,
            4: self.__delete_contact,
            5: self.__count_total_contacts,
            6: self.__search_contact,
        }

        print("\nWelcome to the PhoneBook Application!")
        while True:
            print("\nPlease select an option:")
            print("1. Create contact")
            print("2. View contact")
            print("3. Update contact")
            print("4. Delete contact")
            print("5. Count total contacts")
            print("6. Search contact")
            print("7. Exit")

            try:
                choice = int(input("Enter your choice: ").strip())
                if choice == 7:
                    print("Exiting the program. Goodbye!")
                    break
                elif choice in options:
                    options[choice]()
                else:
                    print("Invalid choice! Please select a valid option.")
            except ValueError:
                print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    PhoneBook.run_script()

