# 417. Pacific Atlantic Water Flow
# Array / DFS / BFS

# https://leetcode.com/problems/pacific-atlantic-water-flow/solution/
# DFS
# running time: faster than 84.24%
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        pr, ar = set(), set()
        
        def dfs(i, j, r):
            r.add((i,j))
            for x, y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                new_i, new_j = i+x, j+y
                if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in r and matrix[new_i][new_j] >= matrix[i][j]:
                    dfs(new_i, new_j, r)
        
        for i in range(m):
            dfs(i, 0, pr)
            dfs(i, n-1, ar)
        for j in range(n):
            dfs(0, j, pr)
            dfs(m-1, j, ar)
        return list(pr.intersection(ar))


# BFS
# runtime: faster than 39.64%
class Solution2:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        pq, aq = deque(), deque()
        for i in range(m):
            pq.append((i,0))
            aq.append((i,n-1))
        for j in range(n):
            pq.append((0, j))
            aq.append((m-1,j))
        
        
        def bfs(queue):
            r = set()
            while queue:
                i, j = queue.popleft()
                r.add((i, j))
                for x, y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    new_i, new_j = i+x, j+y
                    if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in r and matrix[new_i][new_j] >= matrix[i][j]:
                        queue.append((new_i, new_j))
            return r
        
        pr = bfs(pq)
        ar = bfs(aq)
        return list(pr.intersection(ar))