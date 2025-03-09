def greatest_product(grid):
    rows, cols = 20, 20
    max_product = 0

    for r in range(rows):
        for c in range(cols):
            # Check right (horizontal)
            if c + 3 < cols:
                product = grid[r][c] * grid[r][c+1] * grid[r][c+2] * grid[r][c+3]
                max_product = max(max_product, product)
            
            # Check down (vertical)
            if r + 3 < rows:
                product = grid[r][c] * grid[r+1][c] * grid[r+2][c] * grid[r+3][c]
                max_product = max(max_product, product)
            
            # Check diagonal down-right
            if r + 3 < rows and c + 3 < cols:
                product = grid[r][c] * grid[r+1][c+1] * grid[r+2][c+2] * grid[r+3][c+3]
                max_product = max(max_product, product)
            
            # Check diagonal down-left
            if r + 3 < rows and c - 3 >= 0:
                product = grid[r][c] * grid[r+1][c-1] * grid[r+2][c-2] * grid[r+3][c-3]
                max_product = max(max_product, product)
    
    return max_product

# Read input grid
import sys
input_data = sys.stdin.read().splitlines()
grid = [list(map(int, line.split())) for line in input_data]

print(greatest_product(grid))
