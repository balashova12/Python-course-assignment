# notes.py - Simple notes application

# modules
import sys
import datetime
import getpass
import sqliteauthenticate as authenticate
import sqlitedatabase as database
import fetchwebtitle
import jsonnotes
## import insertnoteuser

# main function
def main() -> int:
    # Main loop will run as long as username is not empty.
    while (True):
        # userid is set initially to -1. In this app it means that user is not authenticated.
        userid = -1

        # Login  
        print("\nLogin or just press enter to exit the application.\n")
        username = input("Username: ")
        # Exit main function and application if username is empty
        if (username == ""):
            return 0
        password = getpass.getpass("Password: ")
        userid = authenticate.authenticate(username, password)

        # Main menu
        onmainmenu = True
        while (onmainmenu):
            # Empty line
            print()
            print("Main menu:")
            print("1. Create a note")
            print("2. Retrieve notes")
            print("3. Load a note from a json file")
            print("4. Logout")

            try:
                choice = int(input("Choose and press enter: "))
            except ValueError:
                # if input is not a number
                choice = -1

            # Create a new note
            if choice == 1:
                subject = input("Subject: ")
                text = input("Text: ")
                url = input("Web page (with 'https://' part): ")

                # Initially result is set to -1
                result = -1
                # Create a new note
                result = database.createnote(userid, subject, datetime.datetime.now(), text, url)
                # Print the result
                print("New note created: " + str(result))

            # List notes of current user and open a new menu to access them
            elif choice == 2:
                # Request list of notes
                usernotes = database.listusernotes(userid)

                # List number
                number = 0

                # Fetch details of each note and show them in the menu
                for n in usernotes:
                    print(str(number) + ". " + database.notedetails(n)["subject"])
                    number += 1
                
                # Show details of one note and show note specific menu
                try:
                    selectednote =  int(input("Enter a number of a note of any other number to exit: "))
                except ValueError:
                    # if input is not a number
                    selectednote = -1

                if ((selectednote < len(usernotes)) and (selectednote >= 0)):
                    note = database.notedetails(usernotes[selectednote])
                    print()
                    print("--- --- ---")
                    print("Subject: " + note["subject"])
                    print("Date: " + str(note["date"]))
                    print("Text: " + note["text"])
                    print("Web page: " + note["url"])
                    print("Web title: " + fetchwebtitle.fetchtitle(note["url"]))
                    print("--- --- ---")
                    print()
                    # One new menu loop that is used to delete menu item
                    choice = input("Type \"delete\" to delete this note or press enter to go back: ")

                    if (choice == "Delete"):
                        database.deletenote(usernotes[int(selectednote)])
                        # Reset choice variable as it is used in other menus
                        choice = 0
                    else:
                        # Reset choice variable as it is used in other menus
                        choice = 0

                else:
                    # Reset choice variable as it is used in other menus
                    choice = 0

            elif choice == 3:
                # This try will cover also fails inside jsonnotes module
                try:
                    filename = input("Filename: ")
                    note = jsonnotes.readjsonfile(filename)
                    database.createnote(userid, note["subject"], note["date"], note["text"], note["www"])
                except Exception as error:
                    print(error)

            # Rest of the answers will log user out
            else:
                onmainmenu = False

# main function entry point
if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)