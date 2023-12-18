# CISC 120-91
# assignment10/isvaliddna.py
# Andrei Suslov
# to test this file, run `python isvaliddna.py ATTACGGTTAGC`

"""
1. Function `isValidDNA(dna_string)`:
   - Checks if a given DNA string consists of valid DNA characters ('A', 'C', 'T', 'G').
   - Iterates through each character in the `dna_string` and checks if it belongs to the set of valid characters.
   - Returns `True` if all characters are valid DNA characters; otherwise, returns `False`.
2. Function `main()`:
   - Parses the command-line argument as the DNA string to be validated.
   - Calls the `isValidDNA()` function to check if the provided DNA string is valid.
   - Writes the result (`True` or `False`) to the standard output using `stdio.writeln()`.
"""

import sys
import stdio

def isValidDNA(dna_string):
    valid_chars = {'A', 'C', 'T', 'G'}
    for char in dna_string:
        if char not in valid_chars:
            return False
    return True

def main():
    dna_string = sys.argv[1]
    is_valid = isValidDNA(dna_string)
    stdio.writeln(is_valid)

if __name__ == '__main__':
    main()
