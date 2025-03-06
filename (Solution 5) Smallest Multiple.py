import math

# Function to calculate LCM of two numbers
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Function to calculate the LCM of numbers from 1 to N
def lcm_up_to_n(N):
    result = 1
    for i in range(1, N + 1):
        result = lcm(result, i)
    return result

# Main function to handle the input and output
def main():
    # Reading number of test cases
    T = int(input())
    
    # Process each test case
    for _ in range(T):
        N = int(input())
        # Calculate and print the smallest number divisible by all numbers from 1 to N
        print(lcm_up_to_n(N))

# Running the main function
if __name__ == "__main__":
    main()
