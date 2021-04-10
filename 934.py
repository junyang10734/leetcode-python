# 934. Shortest Bridge
# Array / DFS / BFS

# https://blog.csdn.net/fuxuemingzhu/article/details/83716820
# running time: faster than 14.18%
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        self.M, self.N = len(A), len(A[0])
        self.dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = [[0] * self.N for _ in range(self.M)]
        hasFind = False
        que = collections.deque()
        
        for i in range(self.M):
            if hasFind:
                break
            for j in range(self.N):
                if A[i][j] == 1:
                    self.dfs(A, i, j, visited, que)
                    hasFind = True
                    break
        
        step = 0
        while que:
            size = len(que)
            for _ in range(size):
                i, j = que.popleft()
                for d in self.dirs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < self.M and 0 <= y < self.N:
                        visited[x][y] = 1
                        if A[x][y] == 1:
                            return step
                        elif A[x][y] == 0:
                            A[x][y] = 2
                            que.append((x,y))
                        else:
                            continue
            step += 1
        return -1           
                
    def dfs(self, A, i, j, visited, que):
        if visited[i][j]:
            return
        visited[i][j] = 1
        if A[i][j] == 1:
            que.append((i,j))
            A[i][j] = 2
            for d in self.dirs:
                x, y = i + d[0], j + d[1]
                if 0 <= x < self.M and 0 <= y < self.N:
                    self.dfs(A, x, y, visited, que)
        


# BFS + BFS
# runtime: faster than 67.73%
class Solution2:
    def shortestBridge(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        found = False
        x, y = 0, 0
        for i in range(M):
            if found:
                break
            for j in range(N):
                if A[i][j] == 1:
                    x, y = i, j
                    A[i][j] = 2
                    found = True
                    break
        
        island1 = [(x,y)]
        seen = set()
        seen.add((x,y))
        stack = [(x,y)]
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        while stack:
            x, y = stack.pop(0)
            for i,j in dirs:
                x0, y0 = x+i, y+j
                if 0 <= x0 < M and 0 <= y0 < N and (x0, y0) not in seen:
                    if A[x0][y0] == 1:
                        A[x0][y0] = 2
                        island1.append((x0,y0))
                        stack.append((x0,y0))
                        seen.add((x0,y0))
        res = 0
        while island1:
            size = len(island1)
            for _ in range(size):
                x, y = island1.pop(0)
                for i,j in dirs:
                    x0, y0 = x+i, y+j
                    if 0 <= x0 < M and 0 <= y0 < N and (x0, y0) not in seen:
                        if A[x0][y0] == 1:
                            return res
                        elif A[x0][y0] == 0:
                            island1.append((x0, y0))
                            seen.add((x0, y0))
            res += 1
        return -1
        
                