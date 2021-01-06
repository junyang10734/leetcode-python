# 1091. Shortest Path in Binary Matrix
# Array / Stack / BFS

# https://blog.csdn.net/Wonz5130/article/details/104525673
# running time: faster than 85.80%
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        n = len(grid)
        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        que = [(0,0,1)]
        
        while len(que):
            a, b, cnt = que.pop(0)
            if a == n-1 and b == n-1:
                return cnt
            
            for i,j in directions:
                x, y = a+i, b+j
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    que.append((x,y,cnt+1))
                    grid[x][y] = 1
                    
        return -1
