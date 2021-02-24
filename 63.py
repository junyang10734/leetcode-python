# 63. Unique Paths II
# DP
# Compare with 62, 64

# runtime: faster than 60.67%
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 and obstacleGrid[i][j] == 0:
                    grid[i][j] = 1
                else:
                    if obstacleGrid[i][j] == 0:
                        top = grid[i-1][j] if (i > 0 and obstacleGrid[i-1][j] == 0) else 0
                        left = grid[i][j-1] if (j > 0 and obstacleGrid[i][j-1] == 0) else 0
                        grid[i][j] = top + left
        return grid[-1][-1]