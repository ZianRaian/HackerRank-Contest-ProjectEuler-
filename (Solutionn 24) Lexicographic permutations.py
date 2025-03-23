import sys
from math import factorial

# Precompute factorials up to 13!
fact = [1] * 14
for i in range(2, 14):
    fact[i] = fact[i - 1] * i

def find_nth_permutation(n):
    chars = list("abcdefghijklm")  # Fixed set of characters
    n -= 1  # Convert to zero-based index
    result = []

    # Construct the N-th permutation
    for i in range(13, 0, -1):
        idx = n // fact[i - 1]  # Find index of next character
        result.append(chars[idx])  # Add to result
        del chars[idx]  # Faster than .pop(idx)
        n %= fact[i - 1]  # Update N for next step

    return ''.join(result)

# Read input
T = int(sys.stdin.readline().strip())
output = []  # Use a list for fast output buffering

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    output.append(find_nth_permutation(N))  # Store result in list

sys.stdout.write("\n".join(output) + "\n")  # Fast output
