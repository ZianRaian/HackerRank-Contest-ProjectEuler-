import sys

def compute_collatz(limit):
    """ Precompute longest Collatz sequences up to `limit`. """
    dp = [0] * (limit + 1)
    max_num = [0] * (limit + 1)
    
    dp[1] = 1  # Base case
    max_length, max_value = 1, 1

    for i in range(2, limit + 1):
        n, count = i, 0
        temp = []
        
        # Compute chain length
        while n >= i or dp[n] == 0:
            temp.append(n)
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            count += 1
        
        # Use memoization
        chain_length = count + dp[n]
        for index, val in enumerate(temp):
            if val <= limit:
                dp[val] = chain_length - index
        
        # Track max length number
        if dp[i] >= max_length:
            max_length = dp[i]
            max_value = i
        
        max_num[i] = max_value  # Store the number with longest sequence at `i`
    
    return max_num

# Read input and process
def solve():
    # Read all input at once (faster for large T)
    input_data = sys.stdin.read().split()
    T = int(input_data[0])
    queries = list(map(int, input_data[1:T + 1]))
    
    # Precompute results up to the maximum `N`
    max_N = max(queries)
    max_num = compute_collatz(max_N)

    # Answer each query in O(1)
    results = [str(max_num[n]) for n in queries]
    sys.stdout.write("\n".join(results) + "\n")

# Execute the solution
solve()
