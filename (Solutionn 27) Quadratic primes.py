import sys

def sieve(limit):
    """ Generate a list of primes up to 'limit' using the Sieve of Eratosthenes. """
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    return is_prime

def is_prime(n, primes_set):
    """ Check if a number 'n' is prime using a precomputed prime set. """
    if n < 2:
        return False
    if n in primes_set:
        return True
    return all(n % p != 0 for p in range(2, int(n**0.5) + 1))

def find_best_coefficients(N):
    """ Find the coefficients (a, b) that produce the maximum number of consecutive primes. """
    
    limit = 2 * N * N  # Conservative upper bound for primes
    prime_list = sieve(limit)
    primes_set = {i for i, prime in enumerate(prime_list) if prime}

    best_a, best_b, max_primes = 0, 0, 0

    for a in range(-N, N + 1):
        for b in range(-N, N + 1):
            n = 0
            while is_prime(n * n + a * n + b, primes_set):
                n += 1

            if n > max_primes:
                best_a, best_b, max_primes = a, b, n

    print(best_a, best_b)

# Read input and execute the function
N = int(sys.stdin.readline().strip())
find_best_coefficients(N)
