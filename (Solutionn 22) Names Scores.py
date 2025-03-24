import sys

def name_value(name):
    """Calculate the alphabetical value of a name"""
    return sum(ord(char) - ord('A') + 1 for char in name)

# Read input
N = int(sys.stdin.readline().strip())
names = [sys.stdin.readline().strip() for _ in range(N)]

# Sort names alphabetically
names.sort()

# Precompute name scores
name_scores = {name: (i + 1) * name_value(name) for i, name in enumerate(names)}

# Read and process queries
Q = int(sys.stdin.readline().strip())
output = [str(name_scores[sys.stdin.readline().strip()]) for _ in range(Q)]

# Print all output at once (faster than multiple print calls)
sys.stdout.write("\n".join(output) + "\n")
