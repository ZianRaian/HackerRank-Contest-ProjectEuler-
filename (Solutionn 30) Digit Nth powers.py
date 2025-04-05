def sum_of_digit_powers(number, N):
    """Helper function to calculate the sum of digits of `number` raised to the power `N`."""
    return sum(int(digit) ** N for digit in str(number))

def find_digit_power_numbers(N):
    """Find all numbers that can be written as the sum of Nth powers of their digits."""
    # Upper bound for the search
    max_digit_power = 9 ** N
    upper_limit = (N + 1) * max_digit_power  # A reasonable upper bound to check up to
    
    valid_numbers = []
    for num in range(10, upper_limit):  # Starting from 10 because 1 is not a valid sum
        if num == sum_of_digit_powers(num, N):
            valid_numbers.append(num)
    
    return valid_numbers

# Read the input value
N = int(input().strip())

# Get the valid numbers
valid_numbers = find_digit_power_numbers(N)

# Print the sum of these numbers
print(sum(valid_numbers))
