def sieve_of_eratosthenes(limit):
    # Create a boolean array to mark prime numbers
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    
    # Mark non-primes using the sieve of Eratosthenes
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    # Collect all prime numbers
    primes = [i for i in range(limit + 1) if is_prime[i]]
    return primes

# Precompute primes up to 104,729 (as the 10,000th prime is 104,729)
primes = sieve_of_eratosthenes(104729)

# Read number of test cases
T = int(input())  # Number of test cases

# Process each test case
for _ in range(T):
    N = int(input())  # Read the value of N for each test case
    print(primes[N-1])  # Output the Nth prime (index is N-1 since list is 0-indexed)
