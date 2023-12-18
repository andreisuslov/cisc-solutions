# CISC 120-91
# assignment10/verifypass.py
# Andrei Suslov
# to test this file, run `python verifypass.py Test@123`

"""
1. Function `is_safe_password(password)`:
   - Determines if a given password is safe based on certain criteria.
   - Checks if the password meets the following criteria:
     - Length of at least 8 characters.
     - Contains at least one digit.
     - Contains at least one uppercase letter.
     - Contains at least one lowercase letter.
     - Contains at least one special character (not alphanumeric).
   - Returns `True` if the password meets all criteria; otherwise, returns `False`.
2. Function `main()`:
   - Parses the command-line argument as the password to be verified for safety.
   - Calls the `is_safe_password()` function to check if the provided password is safe.
   - Writes the result (`True` or `False`) to the standard output using `stdio.writeln()`.
"""

import sys
import stdio

def is_safe_password(password):
    if len(password) < 8:
        return False

    contains_digit = any(char.isdigit() for char in password)
    contains_uppercase = any(char.isupper() for char in password)
    contains_lowercase = any(char.islower() for char in password)
    contains_special = any(not char.isalnum() for char in password)

    return contains_digit and contains_uppercase and contains_lowercase and contains_special

def main():
    password = sys.argv[1]
    is_safe = is_safe_password(password)
    stdio.writeln(is_safe)

if __name__ == '__main__':
    main()
