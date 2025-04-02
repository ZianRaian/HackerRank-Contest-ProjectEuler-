MOD = 10**9 + 7

def diagonal_sum(n):
    L = (n - 1) // 2

    # Convert L to MOD space
    L1 = L % MOD
    L2 = (L + 1) % MOD
    L3 = (2 * L + 1) % MOD

    # Modular inverses
    inv2 = pow(2, MOD - 2, MOD)
    inv6 = pow(6, MOD - 2, MOD)

    # Compute each part
    sum_k2 = L1 * L2 % MOD * L3 % MOD * inv6 % MOD
    sum_k = L1 * L2 % MOD * inv2 % MOD
    const = L1

    total = (1 + 16 * sum_k2 % MOD - 8 * sum_k % MOD + 4 * const % MOD) % MOD
    return total

# Read input
import sys
input = sys.stdin.read
data = input().split()

T = int(data[0])
Ns = data[1:]

# Output results
results = []
for i in range(T):
    N = int(Ns[i])
    results.append(str(diagonal_sum(N)))

print('\n'.join(results))
