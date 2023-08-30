import read

RED = "\033[91m"
RESET = "\033[0m"

while True:
    print("\nOptions:")
    print("1. read notes")
    print("2. write a note\n")
    n = int(input("Select option: "))
    if n == 1:
        while True:
            print("\nNotes found: ")
            read.read_filenames()
            n = input("\nType the name of the note you want to read or type 1 to go back: ")
            read.read_note(n)
            if n == "1":
                break
    else:
        print(RED + "Option does not exist!" + RESET)