# Number of Islands

# Mark all elements on the same island as zero and then count the number of 1
# runtime: faster than 99.89% 
# refrence: https://blog.csdn.net/xiaoxiaoley/article/details/82557634
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    res += 1
                    self.dfs(grid, x, y)
        return res

    def dfs(self, grid, x, y):
        grid[x][y] = '0'
        if x-1 >= 0 and grid[x-1][y] == '1':
            self.dfs(grid, x-1, y)
        if x+1 < len(grid) and grid[x+1][y] == '1':
            self.dfs(grid, x+1, y)
        if y-1 >= 0 and grid[x][y-1] == '1':
            self.dfs(grid, x, y-1)
        if y+1 < len(grid[0]) and grid[x][y+1] == '1':
            self.dfs(grid, x, y+1)