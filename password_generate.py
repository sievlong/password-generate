import random
import string
import time

letters = string.ascii_letters  # Alphabet letters (upper and lower case)
digits = string.digits  # All numbers 0-9
symbols = string.punctuation  # All special characters/symbols

print("""
|-----------------------------------|
|---Welcome to password generator---|
|-----------------------------------|
Enter 1: password generator
Enter 2: Exit
""")

while True:
    try:
        user_input = int(input("Please select an option: "))
        if user_input >= 3:
            exit("Please try again")
    except ValueError:
        exit("Hey! That's Not A Number")

    if user_input == 1:
        generate_password = letters
        include_digits = input("Would you like to include digits? [y/n]: ").lower()
        if include_digits == "y":
            generate_password += digits
        include_symbols = input("Would you like to include symbols? [y/n]: ").lower()
        if include_symbols == "y":
            generate_password += symbols
        password = ""
        character_limit = int(input("Length of the password: "))
        for character in range(character_limit):
            password += random.choice(generate_password)
        print(f"Your generated password is: {password}")
    if user_input == 2:
        print("Thank you for using our password generator!")
        break

    time.sleep(1)
    response = input("Would you like to continue: [y/n]")
    if response == "n":
        print("Thank you for using our password generator!")
        break







