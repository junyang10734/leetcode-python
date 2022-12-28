# 785. Is Graph Bipartite?
# similar: 886


# DFS + 染色 - labuladong
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        self.visited = [False] * n
        self.color = [False] * n
        self.res = True

        for node in range(n):
            if not self.visited[node]:
                self.dfs(graph, node)
        return self.res

    def dfs(self, graph, node):
        if not self.res:
            return False
        self.visited[node] = True
        for nx in graph[node]:
            if not self.visited[nx]:
                self.color[nx] = not self.color[node]
                self.dfs(graph, nx)
            else:
                if self.color[nx] == self.color[node]:
                    self.res = False
                    return




# BFS + 染色
# https://blog.csdn.net/fuxuemingzhu/article/details/82788401
# runtime: faster than 79.35%
class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0] * len(graph)  # 0: not visited, 1 - blue, 2 - red
        
        for i in range(len(graph)):
            if graph[i] and visited[i] == 0:
                visited[i] = 1
                q = collections.deque()
                q.append(i)
                while q:
                    v = q.popleft()
                    for e in graph[v]:
                        if visited[e] != 0:
                            if visited[e] == visited[v]:
                                return False
                        else:
                            visited[e] = 3 - visited[v]
                            q.append(e)
        
        return True
        