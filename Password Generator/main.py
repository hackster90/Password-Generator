import random

import string

print(
    """
Password Generator
==================
"""
)

number = int(input("number of passwords?"))
length = int(input("password length?"))


print("\nhere are your passwords:")

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(string.ascii_letters + string.digits)
    print(password)
