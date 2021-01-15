# 417. Pacific Atlantic Water Flow
# Array / DFS

# https://blog.csdn.net/fuxuemingzhu/article/details/82917037
# running time: faster than 65.24%
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        p_visited, a_visited = [[False]*n for _ in range(m)], [[False]*n for _ in range(m)]
        
        for i in range(m):
            self.dfs(p_visited, matrix, m, n, i, 0)
            self.dfs(a_visited, matrix, m, n, i, n-1)
        for j in range(n):
            self.dfs(p_visited, matrix, m, n, 0, j)
            self.dfs(a_visited, matrix, m, n, m-1, j)
        
        res = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i,j])
        return res
            
    
    def dfs(self, visited, matrix, m, n, i, j):
        visited[i][j] = True
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for d in dirs:
            x, y = i + d[0], j + d[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(visited, matrix, m, n, x, y)