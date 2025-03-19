import sys

def max_path_sum(triangle, N):
    # Start from the second last row and move upwards
    for i in range(N-2, -1, -1):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    
    # The top element now contains the maximum path sum
    return triangle[0][0]

# Read input
T = int(sys.stdin.readline().strip())
output = []

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    # Compute max path sum for this triangle
    output.append(str(max_path_sum(triangle, N)))

# Print all results efficiently
sys.stdout.write("\n".join(output) + "\n")
