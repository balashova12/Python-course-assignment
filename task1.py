import datetime
import sys
import getpass

user_accounts = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3",
}

notes = []

def create_note(user):
    subject = input("Enter note subject: ")
    note_text = input("Enter note text: ")
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = {"user": user, "date": date, "subject": subject, "note_text": note_text}
    notes.append(note)
    print("Note created successfully!")

def retrieve_notes(user):
    print(f"Notes for {user}:")
    print()
    headers = ["Date", "Subject", "Note Text"]
    print(f"{headers[0]:<20} {headers[1]:<20} {headers[2]}")
    print("--- --- --- --- ---")
    for note in notes:
        if note["user"] == user:
            print(f"{note['date']:<20} {note['subject']:<20} {note['note_text']}")
    print()

def search_note(user):
    subj = input("Enter the subject of the note you are searching for: ")
    for note in notes:
        if note["user"] == user & note["subject"] == str(subj):
                print(f"{note['user']} - {note['subject']} - {note['notte_text']} - {note['date']}")

def delete_note(user):
    print("Your notes:")
    for i, note in enumerate(notes):
        if note["user"] == user:
            print(f"{i + 1}. {note['subject']} - {note['date']}")
    
    choice = input("Enter the number of the note you want to delete (0 to cancel): ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(notes):
            del notes[index]
            print("Note deleted successfully!")
        elif index == -1:
            print("Deletion canceled.")
        else:
            print("Invalid note number.")
    else:
        print("Invalid input.")

def main():
    user = ""
    while True:
        if user == "":
            print("Welcome to the Note Taking App!")
            username = input("Enter your username (or type 'exit' to quit): ")
            if username == "exit":
                break
            password = getpass.getpass()
            if user_accounts.get(username) == password:
                user = username
                print(f"Welcome, {user}!")
            else:
                print("Invalid username or password. Please try again.")
        else:
            print("Options:")
            print("1. Create a new note")
            print("2. Retrieve and read notes")
            print("3. Search for a note")
            print("4. Delete a note")
            print("5. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                create_note(user)
            elif choice == "2":
                retrieve_notes(user)
            elif choice == "3":
                search_note(user)
            elif choice == "4":
                delete_note(user)
            elif choice == "5":
                user = ""
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    sys.exit(main())