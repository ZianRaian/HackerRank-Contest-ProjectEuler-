def compute_longest_recurring_cycle(limit):
    def get_cycle_length(d):
        remainder = 1
        seen = {}
        pos = 0

        while remainder and remainder not in seen:
            seen[remainder] = pos
            remainder = (remainder * 10) % d
            pos += 1

        return pos - seen[remainder] if remainder else 0

    longest_cycle = [0] * (limit + 1)
    max_d = 0
    max_length = 0

    for d in range(2, limit + 1):
        length = get_cycle_length(d)
        if length > max_length:
            max_length = length
            max_d = d
        longest_cycle[d] = max_d  

    return longest_cycle

# Precompute results up to 10,000
longest_cycle_precomputed = compute_longest_recurring_cycle(10000)

# Handle input
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(longest_cycle_precomputed[n - 1])
