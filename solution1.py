def sum_of_multiples_below(n, k):
    # Calculate the sum of multiples of k below n
    p = (n - 1) // k  # the number of multiples of k below n
    return k * p * (p + 1) // 2

def sum_of_multiples(n):
    # Sum multiples of 3 or 5 below n
    sum_3 = sum_of_multiples_below(n, 3)
    sum_5 = sum_of_multiples_below(n, 5)
    sum_15 = sum_of_multiples_below(n, 15)  # avoid double-counting multiples of 15
    return sum_3 + sum_5 - sum_15

def main():
    # Reading the number of test cases
    t = int(input())
    
    # Reading the inputs for each test case
    for _ in range(t):
        n = int(input())
        # Output the result for each test case
        print(sum_of_multiples(n))

if __name__ == "__main__":
    main()