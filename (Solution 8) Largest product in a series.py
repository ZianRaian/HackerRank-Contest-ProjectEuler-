def find_greatest_product(N, K, number_str):
    max_product = 0
    for i in range(N - K + 1):
        # Get the current window of K digits
        window = number_str[i:i+K]
        
        # Calculate the product of digits in the current window
        product = 1
        for digit in window:
            product *= int(digit)
        
        # Update the maximum product
        max_product = max(max_product, product)
    
    return max_product

# Input reading
T = int(input())  # Number of test cases
for _ in range(T):
    # Read N and K
    N, K = map(int, input().split())
    
    # Read the N digit number as a string
    number_str = input().strip()
    
    # Get the greatest product for this test case
    result = find_greatest_product(N, K, number_str)
    
    # Print the result
    print(result)
