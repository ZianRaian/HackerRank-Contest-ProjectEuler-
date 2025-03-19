import sys

# Zeller's Congruence Formula to determine the day of the week
def day_of_week(y, m, d):
    if m < 3:
        m += 12
        y -= 1
    K = y % 100
    J = y // 100
    day = (d + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) + (5 * J)) % 7
    return day  # 0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday

# Function to count Sundays falling on the 1st of each month
def count_sundays(y1, m1, d1, y2, m2, d2):
    count = 0
    
    # Ensure we start from the first of the month
    if d1 > 1:
        m1 += 1
        if m1 > 12:
            m1 = 1
            y1 += 1

    # Iterate through each month
    while (y1 < y2) or (y1 == y2 and m1 <= m2):
        if day_of_week(y1, m1, 1) == 1:  # If the 1st is Sunday
            count += 1

        # Move to the next month
        m1 += 1
        if m1 > 12:
            m1 = 1
            y1 += 1
    
    return count

# Read input
T = int(sys.stdin.readline().strip())
output = []
for _ in range(T):
    y1, m1, d1 = map(int, sys.stdin.readline().strip().split())
    y2, m2, d2 = map(int, sys.stdin.readline().strip().split())
    output.append(str(count_sundays(y1, m1, d1, y2, m2, d2)))

# Print all results efficiently
sys.stdout.write("\n".join(output) + "\n")
