import sys

def first_ten_digits_of_sum():
    # Read N (number of lines)
    N = int(sys.stdin.readline().strip())

    # Sum all numbers
    total_sum = sum(int(sys.stdin.readline().strip()) for _ in range(N))

    # Print first 10 digits of the sum
    print(str(total_sum)[:10])

# Execute function
first_ten_digits_of_sum()
