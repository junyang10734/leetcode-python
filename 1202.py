# 1202. Smallest String With Swaps
# Union-Find

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]
    
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
    
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)

        for p0, p1 in pairs:
            uf.union(p0, p1)
        
        d = collections.defaultdict(list)
        for idx, p in enumerate(uf.parent):
            k = uf.find(p)
            d[k].append(idx)
        
        res = [0]*n
        for v in d.values():
            v.sort()
            arr = []
            for i in v:
                arr.append(s[i])
            arr.sort()
            for i in range(len(v)):
                res[v[i]] = arr[i]
        return ''.join(res)
      