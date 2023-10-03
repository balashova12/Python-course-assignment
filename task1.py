user_accounts = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3",
}

def create_note(user):
    pass

def retrieve_notes(user):
    pass

def delete_note(user):
    pass

def main():
    user = ""
    while True:
        if user == "":
            pass
        else:
            print("Options:")
            print("1. Create a new note")
            print("2. Retrieve and read notes")
            print("3. Delete a note")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                create_note(user)
            elif choice == "2":
                retrieve_notes(user)
            elif choice == "3":
                delete_note(user)
            elif choice == "4":
                user = ""
            else:
                print("Invalid choice. Please try again.")
