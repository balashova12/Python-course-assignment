import datetime

user_accounts = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3",
}

notes = []

def create_note(user):
    subject = input("Enter note subject: ")
    note_text = input("Enter note text: ")
    date = datetime.datetime.now()
    note = {"user": user, "date": date, "subject": subject, "note_text": note_text}
    notes.append(note)
    print("Note created successfully!")

def retrieve_notes(user):
    print(f"Notes for {user}:")
    for note in notes:
        if note["user"] == user:
            print(f"Date: {note['date']}")
            print(f"Subject: {note['subject']}")
            print(f"Note Text: {note['note_text']}")
            print()

def delete_note(user):
    pass

def main():
    user = ""
    while True:
        if user == "":
            print("Welcome to the Note Taking App!")
            username = input("Enter your username (or type 'exit' to quit): ")
            if username == "exit":
                break
            password = input("Password: ")
            if user_accounts.get(username) == password:
                user = username
                print("Welcome, " + user + "!")
            else:
                print("Invalid username or password. Please try again.")
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
