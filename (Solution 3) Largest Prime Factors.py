import sys
import math

def largest_prime_factor(n):
    # Step 1: Remove all factors of 2
    while n % 2 == 0:
        max_prime = 2
        n //= 2
    
    # Step 2: Check odd factors from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i
    
    # Step 3: If n is still > 1, it's a prime number
    if n > 1:
        max_prime = n
    
    return max_prime

# Fast Input Handling
if __name__ == "__main__":
    input_data = sys.stdin.read().splitlines()
    T = int(input_data[0])  # Number of test cases
    results = []

    for i in range(1, T + 1):
        N = int(input_data[i])
        results.append(str(largest_prime_factor(N)))
    
    print("\n".join(results))
