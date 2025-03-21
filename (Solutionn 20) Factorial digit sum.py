import sys
import math

# Precompute factorials and their digit sums up to 1000
MAX_N = 1000
factorial_sums = [0] * (MAX_N + 1)

# 0! = 1! = 1, so their digit sum is 1
factorial_sums[0] = factorial_sums[1] = 1

# Compute and store factorial digit sums for 2 to 1000
for i in range(2, MAX_N + 1):
    factorial_sums[i] = sum(int(digit) for digit in str(math.factorial(i)))

# Read input
T = int(sys.stdin.readline().strip())
output = []

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    output.append(str(factorial_sums[N]))

# Print all results efficiently
sys.stdout.write("\n".join(output) + "\n")
