import sys

def sieve_of_eratosthenes(n):
    sieve = [True] * (n+1)
    sieve[0], sieve[1] = False, False 
    
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    
    return [i for i, v in enumerate(sieve) if v]

n = int(sys.argv[1])
primes = sieve_of_eratosthenes(n)
print(len(primes))