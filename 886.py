# Possible Bipartition
# DFS

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