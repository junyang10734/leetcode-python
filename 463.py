# Island Perimeter
# Array


# runtime: faster than 11.11% 
class Solution1:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0:
                        up = 0
                    else:
                        up = grid[i-1][j]
                    
                    if j == 0:
                        left  = 0
                    else:
                        left = grid[i][j-1]
                    
                    if i == m - 1:
                        down = 0
                    else:
                        down = grid[i+1][j]
                    
                    if j == n - 1:
                        right = 0
                    else:
                        right = grid[i][j+1]
                    
                    res += 4 - up - down - left - right
        return res


# runtime: faster than 95.39%
class Solution2:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    
                    if i > 0 and grid[i-1][j]:
                        res -= 2
                    
                    if j > 0 and grid[i][j-1]:
                        res -= 2
        return res