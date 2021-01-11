# 399. Evaluate Division
# DFS / Graph

# https://blog.csdn.net/fuxuemingzhu/article/details/82591165
# running time: faster than 18.35%
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (x,y), value in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1.0 / value
        
        ans = [self.dfs(x, y, graph, set()) if x in graph and y in graph else -1.0 for (x,y) in queries]
        return ans
    
    def dfs(self, x, y, graph, visited):
        if x == y:
            return 1.0
        visited.add(x)
        for n in graph[x]:
            if n in visited:
                continue
            visited.add(n)
            d = self.dfs(n, y, graph, visited)
            if d > 0:
                return d*graph[x][n]
        return -1.0
            