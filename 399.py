# 399. Evaluate Division
# Graph

# DFS
# https://blog.csdn.net/fuxuemingzhu/article/details/82591165
# running time: faster than 67.68%
class Solution1:
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



# Union-Find
# https://zxi.mytechroad.com/blog/graph/leetcode-399-evaluate-division/
# runtime: faster than 88.07%
class Solution2:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def find(x):
            if x != UF[x][0]:
                px, pv = find(UF[x][0])
                UF[x] = (px, UF[x][1] * pv)
            return UF[x]
        
        def union(x, y):
            rx, vx = find(x)
            ry, vy = find(y)
            if rx != ry:
                return -1.0
            return vx / vy
        
        
        UF = {}
        for (x,y), v in zip(equations, values):
            if x not in UF and y not in UF:
                UF[x] = (y, v)
                UF[y] = (y, 1.0)
            elif x not in UF:
                UF[x] = (y, v)
            elif y not in UF:
                UF[y] = (x, 1.0/v)
            else:
                rx, vx = find(x)
                ry, vy = find(y)
                UF[rx] = (ry, v/vx*vy)
        
        res = [union(x,y) if x in UF and y in UF else -1.0 for x,y in queries]
        return res       