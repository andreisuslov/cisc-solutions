# NAME
"""
# --------------------------------------------------
# integers.py
# Andrei Suslov
# CISC 120-91
# --------------------------------------------------
"""

# DESCRIPTION
"""
# --------------------------------------------------
# A module with functions that are designed to help
# deal with most basic integer tasks.
# --------------------------------------------------
"""

# FUNCTIONS

# -------------------------------------------------------

def isprime(variable):
    """
    Answers the Question: Is this number Prime?
    Finds if the given number is a Prime Number or not.
    Returns a boolean True or False Statement to the question.
    """
    if variable < 2:
        return "INVALID INTEGER: Only accepts input of integers higher than 1"

    for i in range(2, int(variable ** 0.5) + 1):
        if variable % i == 0:
            return False

    return True if variable > 1 else False

# --------------------------------------------------------

def isrelativeprime(a, b):
    """
    Checks to see if two numbers are relatively Prime.
    Returns a True or False Boolean Statement.
    """
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return gcd(a, b) == 1

# ---------------------------------------------------------

def factors(a):
    """
    Returns the factors of an integer.
    """
    return [i for i in range(1, a + 1) if a % i == 0]

# ----------------------------------------------------------

def divisor(a, b):
    """
    Returns the greatest common divisor of two numbers.
    """
    while b:
        a, b = b, a % b
    return a

# -----------------------------------------------------------

def multiple(a, b):
    """
    Returns the least common multiple of two parameters.
    """
    return abs(a * b) // divisor(a, b) if a and b else 0

# -------------------------------------------------------

def totient(n):
    """
    Returns the totient function output for an "n" input.
    """
    if n <= 1:
        return "INVALID INTEGER: Only accepts input of integers higher than 1"

    if isprime(n):
        return n - 1

    count = sum(1 for i in range(1, n) if isrelativeprime(n, i))
    return count

# --------------------------------------------------------------

def isodd(a):
    """
    Answers the question: Is this integer odd? Returns True or False.
    """
    return a % 2 != 0

# --------------------------------------------------------------

def iseven(a):
    """
    Answers the question: Is this integer even? Returns True or False.
    """
    return a % 2 == 0

# --------------------------------------------------------------

# TESTS

def main():
    import sys

    if len(sys.argv) < 3:
        print("Usage: python integers.py <integer1> <integer2>")
        return

    try:
        v1 = int(sys.argv[1])
        v2 = int(sys.argv[2])
    except ValueError:
        print("Please enter valid integers.")
        return

    print("----------------")
    print("isprime Test")
    print(f"Is {v1} prime? {isprime(v1)}")
    print("----------------")

    print()
    print()

    print("----------------")
    print("isrelativeprime Test")
    print(f"Are {v1} and {v2} relatively prime? {isrelativeprime(v1, v2)}")
    print("----------------")

    print()
    print()

    print("----------------")
    print("factors Test")
    print(f"Factors of {v1}: {factors(v1)}")
    print("----------------")

    print()
    print()

    print("----------------")
    print("divisor Test")
    print(f"Greatest common divisor of {v1} and {v2}: {divisor(v1, v2)}")
    print("----------------")

    print()
    print()

    print("----------------")
    print("multiple Test")
    print(f"Least common multiple of {v1} and {v2}: {multiple(v1, v2)}")
    print("----------------")

    print()
    print()

    print("----------------")
    print("totient Test")
    print(f"Euler's Totient function of {v1}: {totient(v1)}")
    print("----------------")

    print()
    print()

    print("----------------")
    print("isodd Test")
    print(f"Is {v1} odd? {isodd(v1)}")
    print("----------------")

    print()
    print()

    print("----------------")
    print("iseven Test")
    print(f"Is {v1} even? {iseven(v1)}")
    print("----------------")

if __name__ == '__main__':
    main()
