import random
import string

def generate_password():
    # Taking user input for password length
    length = int(input("Enter the length of the password: "))

    # Taking user input for character set options
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    # Creating a pool of characters based on user choices
    characters = string.ascii_lowercase  # Always include lowercase letters

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if len(characters) == 0:
        print("No character sets selected! Exiting...")
        return

    # Generating the password
    password = ''.join(random.choice(characters) for i in range(length))

    # Displaying the password
    print(f"Generated Password: {password}")

# Call the function
generate_password()
