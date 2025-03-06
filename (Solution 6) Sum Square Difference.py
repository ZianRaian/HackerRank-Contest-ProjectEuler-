def absolute_difference(N):
    sum_of_squares = N * (N + 1) * (2 * N + 1) // 6
    sum_of_numbers = N * (N + 1) // 2
    square_of_sum = sum_of_numbers * sum_of_numbers
    return abs(square_of_sum - sum_of_squares)

# Input
T = int(input())  # Number of test cases

# Process each test case
for _ in range(T):
    N = int(input())  # Value of N for the current test case
    print(absolute_difference(N))
