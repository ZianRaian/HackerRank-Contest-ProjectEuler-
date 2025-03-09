def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for start in range(2, int(limit ** 0.5) + 1):
        if primes[start]:
            for multiple in range(start * start, limit + 1, start):
                primes[multiple] = False
    prime_sums = [0] * (limit + 1)
    current_sum = 0
    for num in range(limit + 1):
        if primes[num]:
            current_sum += num
        prime_sums[num] = current_sum
    return prime_sums

limit = 10**6
prime_sums = sieve(limit)

T = int(input())
for _ in range(T):
    N = int(input())
    print(prime_sums[N])