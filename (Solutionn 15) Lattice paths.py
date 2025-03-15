import sys

MOD = 10**9 + 7
MAX = 1000  # Max possible value of (N + M)

# Precompute Factorials & Modular Inverses
fact = [1] * (MAX + 1)
inv_fact = [1] * (MAX + 1)

def power_mod(x, y, mod):
    result = 1
    while y > 0:
        if y % 2:
            result = (result * x) % mod
        x = (x * x) % mod
        y //= 2
    return result

# Precompute factorials and modular inverses using Fermat's theorem
for i in range(2, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[MAX] = power_mod(fact[MAX], MOD - 2, MOD)  # Compute inverse of MAX! using Fermat's theorem
for i in range(MAX - 1, 0, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
inv_fact[0] = 1  # By definition

# Function to compute binomial coefficient C(n, k) % MOD
def binomial(n, k):
    if k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

# Fast Input Reading & Output Writing
T = int(sys.stdin.readline().strip())
output = []
for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    output.append(str(binomial(N + M, N)))

sys.stdout.write("\n".join(output) + "\n")
