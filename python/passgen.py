# password generator 
# choose lenght of password
# can use multiples of these: lowercase, uppercase, numbers and symbols

import random

def passwdgen():
    upcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowcase = upcase.lower()
    digits = "0123456789"
    symbols = "()[],;:.-_/\\?+*&^%$#@!"

    all = ""

    # user gives input that is compared to conditions and set according to user input
    print("Type y or n accordingly")
    upper = input("Use uppercase? y/n ")
    lower = input("Use lowercase? y/n ")
    nums = input("Use digits? y/n ")
    symb = input("Use symbols? y/n ")

    if upper == 'y':
        all = all + upcase
    if lower == 'y':
        all = all + lowcase
    if nums == 'y':
        all = all + digits
    if symb == 'y':
        all = all + symbols

    passlen = int(input("Please enter the lenght of the password you wish to generate: "))
    password = "".join(random.choices(all, passlen))
    print(password)

passwdgen()
