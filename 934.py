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
        