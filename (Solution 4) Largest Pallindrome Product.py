def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_below_n(N):
    for num in range(N - 1, 101101 - 1, -1):
        if is_palindrome(num):
            for i in range(999, 99, -1):
                if num % i == 0:
                    j = num // i
                    if 100 <= j <= 999:
                        return num
    return -1  # Should never reach here as a valid answer always exists.

# Read input
T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    print(largest_palindrome_below_n(N))
