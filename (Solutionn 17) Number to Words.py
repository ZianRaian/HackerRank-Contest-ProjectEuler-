import sys

# Mappings for English words
ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
        "Seventeen", "Eighteen", "Nineteen"]

TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

UNITS = ["", "Thousand", "Million", "Billion"]

# Function to convert three-digit numbers to words
def three_digit_to_words(num):
    if num == 0:
        return ""
    
    result = []
    
    # Handle Hundreds place
    if num >= 100:
        result.append(ONES[num // 100] + " Hundred")
        num %= 100
    
    # Handle 1-19 directly
    if 1 <= num < 20:
        result.append(ONES[num])
    elif num >= 20:
        result.append(TENS[num // 10])
        if num % 10:
            result.append(ONES[num % 10])
    
    return " ".join(result).strip()

# Main function to convert a number into words
def number_to_words(num):
    if num == 0:
        return "Zero"

    result = []
    unit_index = 0

    while num > 0:
        part = num % 1000
        if part > 0:
            result.append(three_digit_to_words(part) + (" " + UNITS[unit_index] if unit_index > 0 else ""))
        num //= 1000
        unit_index += 1

    return " ".join(result[::-1]).strip()

# Read Input
T = int(sys.stdin.readline().strip())
output = []
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    output.append(number_to_words(N))

# Print output efficiently
sys.stdout.write("\n".join(output) + "\n")
