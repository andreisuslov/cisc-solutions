# stresstest1.py
# Andrei Suslov
# CISC 120-91

import random
from integers import isprime, factors, totient

def stress_test(num_tests=500, max_int=1000):
    """Perform a stress test on prime and totient functions in the integers module."""
    for _ in range(num_tests):
        # Generate a random integer
        a = random.randint(1, max_int)

        # Test the isprime function
        prime_result = isprime(a)
        print(f"Testing isprime({a}): {prime_result}")

        # Test the factors function
        factors_result = factors(a)
        print(f"Testing factors({a}): {factors_result}")

        # Test the totient function
        totient_result = totient(a)
        print(f"Testing totient({a}): {totient_result}")

        # Divider for readability
        print("-" * 40)

# Run the stress test
if __name__ == "__main__":
    stress_test()
