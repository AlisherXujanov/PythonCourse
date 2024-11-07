# 1. Write a Python program that defines a function and takes a password string
# as input and returns its SHA-256 hashed representation as a hexadecimal string.

import hashlib
def hash_password(password):
    # Encode the password as bytes
    password_bytes = password.encode('utf-8')

    # Use SHA-256 hash function to create a hash object
    hash_object = hashlib.sha256(password_bytes)

    # Get the hexadecimal representation of the hash
    password_hash = hash_object.hexdigest()

    return password_hash


password = input("Input your password: ")
hashed_password = hash_password(password)
print(f"Your hashed password is: {hashed_password}")

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# 2.  Write a Python program to check if a password meets the following criteria:
# At least 8 characters long and
# Contains at least one uppercase letter, one lowercase letter, one digit, 
# and one special character (!, @ ,  # , $, %, or &)
# If the password meets the criteria, print a message that says "Valid Password." 
# If it doesn't meet the criteria, print a message that says "Password does not meet requirements."

def check_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check if the password contains at least one special character
    special_characters = ['!', '@', '#', '$', '%', '&']
    if not any(char in special_characters for char in password):
        return False

    return True

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

# 3.  Write a Python program that creates a password strength meter. 
# The program should prompt the user to enter a password and check its 
# strength based on criteria such as length, complexity, and randomness. 
# Afterwards, the program should provide suggestions for improving the password's strength.
def password_strength(password):
    # Check the length of the password
    suggestions = []
    
    length = len(password)
    if length < 8:
        suggestions.append("Password is too short. Please enter a password with at least 8 characters.")
    elif length < 12:
        suggestions.append("Password length is okay, but consider making it longer for better security.")
    else:
        suggestions.append("Password length is good.")

    # Check the complexity of the password
    complexity = 0
    if any(char.isupper() for char in password):
        complexity += 1
    if any(char.islower() for char in password):
        complexity += 1
    if any(char.isdigit() for char in password):
        complexity += 1
    special_characters = ['!', '@', '#', '$', '%', '&']
    if any(char in special_characters for char in password):
        complexity += 1

    if complexity < 3:
        suggestions.append("Password complexity is low. Consider adding more variety of characters.")
    elif complexity < 4:
        suggestions.append("Password complexity is okay, but consider adding more variety of characters.")
    else:
        suggestions.append("Password complexity is good.")

    # Check the randomness of the password
    if len(set(password)) < length:
        suggestions.append("Password is not very random. Consider adding more unique characters.")

    return suggestions


password = input("Enter your password: ")
suggestions = password_strength(password)
print("Password strength suggestions:")
for index, suggestion in enumerate(suggestions):
    print(f"{index+1}. {suggestion}")
    print("----------------------------------------------")



# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# 4. Write a Python program that simulates a brute-force attack on a password by 
# trying out all possible character combinations.
import itertools
def brute_force_attack(password):
    # Define the set of characters that can be used in the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&"
    attempts = 0

    # Iterate over all possible password lengths
    for length in range(1, 9):
        # Generate all possible combinations of characters of the given length
        for combination in itertools.product(characters, repeat=length):
            # Convert the combination to a string
            attempt = "".join(combination)
            attempts += 1

            # Check if the attempt matches the password
            if attempt == password:
                return attempts

    return attempts
