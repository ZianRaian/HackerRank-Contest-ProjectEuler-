import math

def precompute_fibonacci_digits(limit):
    phi = (1 + math.sqrt(5)) / 2  # Golden ratio
    sqrt5_log = math.log10(math.sqrt(5))
    phi_log = math.log10(phi)
    
    fibonacci_digits = [0] * (limit + 1)
    
    for n in range(2, limit + 1):
        fibonacci_digits[n] = math.ceil((n - 1 + sqrt5_log) / phi_log)
    
    return fibonacci_digits

# Precompute results for N up to 5000
fib_digits_precomputed = precompute_fibonacci_digits(5000)

# Handle input
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(fib_digits_precomputed[n])
