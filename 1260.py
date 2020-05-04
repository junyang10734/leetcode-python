# Shift 2D Grid
# Array

# runtime: faster than 11.72%
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        res = grid
        
        while k>0:
            final_v = grid[n-1][m-1]
            for i in range(n-1,-1,-1):
                for j in range(m-1,-1,-1):
                    if j!=0:
                        grid[i][j] = grid[i][j-1]
                    elif i != 0 and j == 0:
                        grid[i][j] = grid[i-1][m-1]
                    elif i== 0 and j == 0:
                        grid[i][j] = final_v
            k -= 1
        
        return grid