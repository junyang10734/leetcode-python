# 1254. Number of Closed Islands
# DFS / 岛屿问题
# compare: 1020

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            # 把靠左边的岛屿淹掉
            self.dfs(grid, i, 0)
            # 把靠右边的岛屿淹掉
            self.dfs(grid, i, n-1)
        for j in range(n):
            # 把靠上边的岛屿淹掉
            self.dfs(grid, 0, j)
            # 把靠下边的岛屿淹掉
            self.dfs(grid, m-1, j)
        
        res = 0
        # 遍历 grid，剩下的岛屿都是封闭岛屿
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    self.dfs(grid, i, j)

        return res

    # 从 (i, j) 开始，将与之相邻的陆地都变成海水 
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return
        
        if grid[i][j] == 1:
            return
        
        grid[i][j] = 1
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # 淹没上下左右的陆地
        for x,y in dirs:
            self.dfs(grid, x+i, y+j)