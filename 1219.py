# 1219. Path with Maximum Gold
# Array / DFS

# https://blog.csdn.net/Orientliu96/article/details/103423021
# running time: faster than 85.77%
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        self.res = 0
        
        def dfs(x,y,gold):
            self.res = max(self.res, gold)
            for (i,j) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0 <= i < m and 0 <= j < n and grid[i][j] != 0:
                    v = grid[i][j]
                    grid[i][j] = 0
                    dfs(i,j,gold+v)
                    grid[i][j] = v
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    x = grid[i][j]
                    grid[i][j] = 0
                    dfs(i,j, x)
                    grid[i][j] = x
        
        return self.res