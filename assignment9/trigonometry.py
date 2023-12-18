# NAME
"""
# --------------------------------------------------
# trigonometry.py
# Andrei Suslov
# CISC 120-91
# --------------------------------------------------
"""

# DESCRIPTION
"""
# --------------------------------------------------
# A module with functions for basic trigonometric
# operations including sine, cosine, tangent, and
# their hyperbolic counterparts.
# --------------------------------------------------
"""

# FUNCTIONS

# -------------------------------------------------------

import math

def sin(x):
    """Calculate the sine of x (x in radians)."""
    return math.sin(x)

def cos(x):
    """Calculate the cosine of x (x in radians)."""
    return math.cos(x)

def tan(x):
    """Calculate the tangent of x (x in radians)."""
    return math.tan(x)

def sinh(x):
    """Calculate the hyperbolic sine of x."""
    return (math.exp(x) - math.exp(-x)) / 2

def cosh(x):
    """Calculate the hyperbolic cosine of x."""
    return (math.exp(x) + math.exp(-x)) / 2

def tanh(x):
    """Calculate the hyperbolic tangent of x."""
    return sinh(x) / cosh(x)

def sech(x):
    """Calculate the hyperbolic secant of x."""
    if cosh(x) == 0:
        raise ValueError("sech(x) is undefined for cosh(x) = 0")
    return 1 / cosh(x)

def csch(x):
    """Calculate the hyperbolic cosecant of x."""
    if sinh(x) == 0:
        raise ValueError("csch(x) is undefined for sinh(x) = 0")
    return 1 / sinh(x)

def coth(x):
    """Calculate the hyperbolic cotangent of x."""
    if tanh(x) == 0:
        raise ValueError("coth(x) is undefined for tanh(x) = 0")
    return 1 / tanh(x)

# --------------------------------------------------------------

def main():
    """Test functions in the trigonometry module."""
    test_values = [0, 0.5, 1, 1.5, 2, 2.5]

    print("Trigonometric functions test:")
    for value in test_values:
        print(f"sin({value}) = {sin(value)}")
        print(f"cos({value}) = {cos(value)}")
        print(f"tan({value}) = {tan(value)}")
        print()

    print("Hyperbolic functions test:")
    for value in test_values:
        print(f"sinh({value}) = {sinh(value)}")
        print(f"cosh({value}) = {cosh(value)}")
        print(f"tanh({value}) = {tanh(value)}")
        print(f"sech({value}) = {sech(value)}")

        try:
            print(f"csch({value}) = {csch(value)}")
        except ValueError as e:
            print(f"csch({value}) is undefined: {e}")

        try:
            print(f"coth({value}) = {coth(value)}")
        except ValueError as e:
            print(f"coth({value}) is undefined: {e}")
        
        print()

if __name__ == "__main__":
    main()

