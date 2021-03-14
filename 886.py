# Possible Bipartition
# Graph / Graph Coloring

# DFS
# https://leetcode.com/problems/possible-bipartition/solution/
# runtime: faster than 42.12% 
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color = {}
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(n, c^1) for n in graph[node])
        
        return all(dfs(node) for node in range(1, N+1) if node not in color)


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
                    