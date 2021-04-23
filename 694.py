# 694. Number of Distinct Islands
# DFS

# https://leetcode.com/problems/number-of-distinct-islands/discuss/108480/Simple-Python-169ms
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islands.add(self.dfs(grid,i,j,'s'))
        return len(islands)
    
    def dfs(self, grid, i, j, path):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return ''
        
        grid[i][j] = 0
        return path + self.dfs(grid, i+1, j, 'd') + 'u' + self.dfs(grid, i-1, j, 'u') + 'd' + self.dfs(grid, i, j+1, 'r') + 'l' + self.dfs(grid, i, j-1, 'l') + 'r'