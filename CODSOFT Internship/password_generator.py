"""
Password Generator Module.

This module generates a random password based on user input for the number of
alphabets, numbers, and special characters.
"""

import string
import random

print("Welcome to password generator.")

alphabets = int(input("Enter number of alphabets: "))
numbers = int(input("Enter number of numbers: "))
special = int(input("Enter number of special characters: "))

ALPHABETS = string.ascii_letters
NUMBERS = string.digits
SPECIAL_CHARACTERS = "!@#$%^&*()_+-=[]{}|;:',.<>/?"

password = ''

password += ''.join(random.choice(ALPHABETS) for _ in range(1, alphabets+1))
password += ''.join(random.choice(NUMBERS) for _ in range(1, numbers+1))
password += ''.join(random.choice(SPECIAL_CHARACTERS) for _ in range(1, special+1))

pass_list = list(password)
random.shuffle(pass_list)

final_password = ''.join(pass_list)
print(final_password)