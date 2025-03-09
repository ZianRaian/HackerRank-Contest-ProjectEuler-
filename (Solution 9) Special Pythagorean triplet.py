def max_pythagorean_triplet(n):
    max_product = -1
    
    for a in range(1, n // 3):
        b = (n**2 - 2 * n * a) // (2 * (n - a))
        c = n - a - b
        
        if a < b < c and a**2 + b**2 == c**2:
            max_product = max(max_product, a * b * c)
    
    return max_product

# Read input
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(max_pythagorean_triplet(n))