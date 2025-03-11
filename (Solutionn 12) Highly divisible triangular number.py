import sys
import math

def count_divisors(n):
    """Returns the number of divisors of n using optimized factorization."""
    if n == 1:
        return 1
    count = 0
    sqrt_n = int(math.sqrt(n))
    
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2 if i * i != n else 1  # Count both factors unless it's a perfect square
    return count

def precompute_triangle_numbers(limit):
    """Precomputes the first triangle number with more than N divisors up to limit."""
    results = {}
    n = 1
    triangle_number = 1
    
    while len(results) <= limit:
        # Compute number of divisors using optimized method
        if n % 2 == 0:
            divisors = count_divisors(n // 2) * count_divisors(n + 1)
        else:
            divisors = count_divisors(n) * count_divisors((n + 1) // 2)
        
        # Store result if it's the first triangle number with more than k divisors
        if divisors not in results:
            results[divisors] = triangle_number

        # Generate next triangle number
        n += 1
        triangle_number += n
    
    return results

# Read input
T = int(sys.stdin.readline().strip())
queries = [int(sys.stdin.readline().strip()) for _ in range(T)]

# Precompute results for all possible N values in queries
max_N = max(queries) if queries else 1  # Get maximum N from input
triangle_numbers = precompute_triangle_numbers(max_N)

# Answer queries in O(1) time
for N in queries:
    for key in sorted(triangle_numbers.keys()):
        if key > N:
            print(triangle_numbers[key])
            break
