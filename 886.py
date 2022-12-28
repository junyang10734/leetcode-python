# Possible Bipartition
# Graph / Graph Coloring
# similar: 785

# DFS - labuladong
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        self.res = True
        self.visited = [False] * (n+1)
        self.color = [False] * (n+1)

        for v in range(1, n+1):
            if not self.visited[v]:
                self.dfs(graph, v)
        return self.res

    
    def dfs(self, graph, node):
        if not self.res:
            return False
        
        self.visited[node] = True

        for nx in graph[node]:
            if self.visited[nx]:
                if self.color[nx] == self.color[node]:
                    self.res = False
                    return
            else:
                self.color[nx] = not self.color[node]
                self.dfs(graph, nx)



# BFS
# https://blog.csdn.net/fuxuemingzhu/article/details/82827177
# runtime: faster than 89.35%
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = [0]*(N+1)
        for i in range(1, N+1):
            if color[i] != 0:
                continue
            color[i] = 1
            q = deque()
            q.append(i)
            while q:
                node = q.popleft()
                for v in graph[node]:
                    if color[v] != 0:
                        if color[v] == color[node]:
                            return False
                    else:
                        color[v] = 3 - color[node]
                        q.append(v)
        return True
                    