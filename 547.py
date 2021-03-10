# 547. Number of Provinces
# Graph

# DFS
# runtime: faster than 99.28%
class Solution1:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        def dfs(city):
            for nei, connected in enumerate(isConnected[city]):
                if connected and nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        res = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res



# Union-Find
# runtime: faster than 40.70%
class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]
        self.count = n
    
    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, p, q):
        rootp, rootq = self.find(p), self.find(q)
        if rootp == rootq:
            return
        if self.size[rootp] >= self.size[rootq]:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        else:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        self.count -= 1
    
    def getCount(self):
        return self.count
        
class Solution2:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UF(n)
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.getCount()