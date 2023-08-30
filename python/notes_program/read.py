import os

RED = "\033[91m"
RESET = "\033[0m"

def read_note(note):
    print("\n")
    note = "notes/" + note + ".txt"
    try:
        with open(note, "r") as f:
            read_content = f.read()
            print(f"From {note[6:]}: ")
            print(read_content)
    except FileNotFoundError:
        msg = RED + "Sorry, the file " + note + " does not exist." + RESET
        print(msg)

def read_filenames():
    directory_path = "notes"
    filenames = os.listdir(directory_path)
    for filename in filenames:
        if filename.endswith(".txt"):
            print(f"* {filename[:-4]}")
        else:
            print(f"* {filename}")