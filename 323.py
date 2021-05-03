# 323. Number of Connected Components in an Undirected Graph
# Union-Find

class DSU:
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
    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for s,e in edges:
            dsu.union(s, e)
        return dsu.getCount()