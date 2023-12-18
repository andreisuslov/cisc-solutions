# stresstest2.py
# Andrei Suslov
# CISC 120-91

import random
from integers import isrelativeprime, divisor, multiple, isodd, iseven

def stress_test(num_tests=500, max_int=1000):
    """Perform a stress test on divisibility and parity functions in the integers module."""
    for _ in range(num_tests):
        # Generate two random integers
        a = random.randint(1, max_int)
        b = random.randint(1, max_int)

        # Test the isrelativeprime function
        relative_prime_result = isrelativeprime(a, b)
        print(f"Testing isrelativeprime({a}, {b}): {relative_prime_result}")

        # Test the divisor (GCD) function
        gcd_result = divisor(a, b)
        print(f"Testing divisor({a}, {b}): {gcd_result}")

        # Test the multiple (LCM) function
        lcm_result = multiple(a, b)
        print(f"Testing multiple({a}, {b}): {lcm_result}")

        # Test the isodd function
        isodd_result = isodd(a)
        print(f"Testing isodd({a}): {isodd_result}")

        # Test the iseven function
        iseven_result = iseven(a)
        print(f"Testing iseven({a}): {iseven_result}")

        # Divider for readability
        print("-" * 40)

# Run the stress test
if __name__ == "__main__":
    stress_test()
