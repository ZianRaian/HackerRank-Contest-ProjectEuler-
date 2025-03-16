import sys

def power_digit_sum(n):
    """ Computes the sum of digits of 2^N. """
    return sum(map(int, str(2**n)))

def solve():
    # Read all input at once (fast for large T)
    input_data = sys.stdin.read().split()
    T = int(input_data[0])
    queries = map(int, input_data[1:T + 1])
    
    # Compute and print results
    results = [str(power_digit_sum(n)) for n in queries]
    sys.stdout.write("\n".join(results) + "\n")

# Execute solution
solve()
