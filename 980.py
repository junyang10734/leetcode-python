# 980. Unique Paths III
# backtrack

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        emptySquares = 0
        startx, starty = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] >= 0:
                    emptySquares += 1
                if grid[i][j] == 1:
                    startx, starty = i, j
            
        res = 0

        def backtrack(i, j, remain):
            nonlocal res

            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] < 0:
                return

            if grid[i][j] == 2 and remain == 1:
                res += 1
                return
            
            temp = grid[i][j]
            grid[i][j] = -4
            remain -= 1

            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newx, newy = i + x, j + y
                backtrack(newx, newy, remain)
            
            grid[i][j] = temp
        
        backtrack(startx, starty, emptySquares)
        return res
