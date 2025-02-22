import sys

def precompute_even_fib_sums(limit):
    even_fib = [2, 8]  # First two even Fibonacci numbers
    while True:
        next_even = 4 * even_fib[-1] + even_fib[-2]
        if next_even > limit:
            break
        even_fib.append(next_even)
    
    # Precompute prefix sums for fast queries
    prefix_sums = []
    current_sum = 0
    for num in even_fib:
        current_sum += num
        prefix_sums.append((num, current_sum))
    
    return prefix_sums

def find_even_fib_sum(n, precomputed_sums):
    # Binary search to find the largest even Fibonacci number <= n
    left, right = 0, len(precomputed_sums) - 1
    while left <= right:
        mid = (left + right) // 2
        if precomputed_sums[mid][0] > n:
            right = mid - 1
        else:
            left = mid + 1
    return precomputed_sums[right][1] if right >= 0 else 0

def main():
    # Read input
    input_data = sys.stdin.read().split()
    T = int(input_data[0])
    queries = list(map(int, input_data[1:T+1]))

    # Find the max N to optimize precomputation
    max_n = max(queries)
    
    # Precompute Fibonacci sums up to max_n
    precomputed_sums = precompute_even_fib_sums(max_n)
    
    # Answer queries efficiently
    results = [str(find_even_fib_sum(n, precomputed_sums)) for n in queries]
    
    # Output all results in one go for efficiency
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
