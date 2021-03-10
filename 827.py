# 827. Making A Large Island
# DFS + BFS

# runtime: faster than 16.52%
# http://bookshadow.com/weblog/2018/04/29/leetcode-making-a-large-island/
from typing import List
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        marks = [[0]*n for _ in range(n)]
        
        def getArea(sx, sy, mk):
            stack = [(sx, sy)]
            seen = set(stack)
            area = 0
            while stack:
                x, y = stack.pop()
                area += 1
                for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            for x, y in seen:
                marks[x][y] = mk
                grid[x][y] = area
            return area
                
            
        maxArea, mk = 0, 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] and marks[i][j] == 0:
                    mk += 1
                    maxArea = max(maxArea, getArea(i,j,mk))
        
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    area = 0
                    mkset = set()
                    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                        if 0 <= nx < n and 0 <= ny < n and marks[nx][ny] not in mkset:
                            area += grid[nx][ny]
                            mkset.add(marks[nx][ny])
                    maxArea = max(maxArea, area+1)
        
        return maxArea