# notes.py - simple notes application

# modules
import sys

# main function
def main() -> int:
    # login screen
    print("")
    username = input("Username: ")
    # password request needs to be added here
    password = input("Password: ")
    print("")

    # Notes  screen 
    print("1. some text")
    print("2. ...")
    input("Selection: ")

    return(0)

# main function definition
if __name__ == '__main__':
    sys.exit(main())