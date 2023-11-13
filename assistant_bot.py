def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Contact not found"

    return wrapper


contacts = {}


@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} with phone {phone} added successfully."


@input_error
def change_contact(name, phone):
    if name not in contacts:
        raise IndexError
    contacts[name] = phone
    return f"Contact {name} phone number changed to {phone}."


@input_error
def phone_contact(name):
    if name not in contacts:
        raise IndexError
    return f"The phone number for {name} is {contacts[name]}."


@input_error
def show_all_contacts():
    if not contacts:
        return "No contacts found."
    result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return result


def main():
    print("How can I help you?")

    while True:
        user_input = input().lower()

        if user_input == "good bye" or user_input == "close" or user_input == "exit":
            print("Good bye!")
            break

        elif user_input == "hello":
            print("How can I help you?")

        elif user_input.startswith("add"):
            _, name, phone = user_input.split()
            print(add_contact(name, phone))

        elif user_input.startswith("change"):
            _, name, phone = user_input.split()
            print(change_contact(name, phone))

        elif user_input.startswith("phone"):
            _, name = user_input.split()
            print(phone_contact(name))

        elif user_input == "show all":
            print(show_all_contacts())

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()