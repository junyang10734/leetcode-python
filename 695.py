# Max Area of Island
# Array / Graph / 岛屿问题

# DFS 模板
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, self.dfs(grid, i, j))

        return res


    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return 0
        
        if grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        area = 1
        for x,y in dirs:
            area += self.dfs(grid, x+i, y+j)
        return area


# Depth-First Search (Recursive)
# runtime: faster than 32.59% 
class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r,c) not in seen and grid[r][c]):
                return 0
            seen.add((r,c))
            return (1 + area(r+1, c) + area(r-1, c) + area(r, c-1) + area(r, c+1))
        
        return max(area(r,c) for r in range(len(grid)) for c in range(len(grid[0])))


# Depth-First Search (Iterative)
# runtime: faster than 89.44%
class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ans = 0
        
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans