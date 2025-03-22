import sys

MAX_N = 100000

# Step 1: Precompute sum of proper divisors for all numbers up to MAX_N
divisor_sums = [0] * (MAX_N + 1)

for i in range(1, MAX_N // 2 + 1):  # Iterate only up to MAX_N/2
    for j in range(2 * i, MAX_N + 1, i):
        divisor_sums[j] += i

# Step 2: Identify amicable numbers and store cumulative sums
amicable_sums = [0] * (MAX_N + 1)

for i in range(1, MAX_N + 1):
    d_i = divisor_sums[i]
    if d_i != i and d_i <= MAX_N and divisor_sums[d_i] == i:
        amicable_sums[i] = i

# Step 3: Compute prefix sums for quick lookup
for i in range(1, MAX_N + 1):
    amicable_sums[i] += amicable_sums[i - 1]

# Step 4: Process test cases
T = int(sys.stdin.readline().strip())
output = []
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    output.append(str(amicable_sums[N - 1]))

sys.stdout.write("\n".join(output) + "\n")
