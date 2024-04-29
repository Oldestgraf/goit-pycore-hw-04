def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Invalid command."
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Invalid command."
    else:
        name_str = name[0]
        if name_str in contacts:
            contacts[name] = phone
            return "Contact updated."
        return "Contact not found."

def show_phone(args, contacts):
    try:
        name = args
    except ValueError:
        return "Invalid command."
    else:
        name_str = name[0]
        if name_str in contacts:
            return contacts.get(name_str)
        return "Contact not found."

def show_all(args, contacts):
    if args != []:
        return "Invalid command."
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
