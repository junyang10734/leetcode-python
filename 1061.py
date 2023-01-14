# 1061. Lexicographically Smallest Equivalent String
# Union Find

class UF:
    def __init__(self):
        self.root = {}

    def find(self, p):
        if p not in self.root:
            self.root[p] = p
        else:
            while p != self.root[p]:
                self.root[p] = self.root[self.root[p]]
                p = self.root[p]
        return p
    
    def union(self, p, q):
        rootp, rootq = self.find(p), self.find(q)
        if rootp == rootq:
            return 
        elif rootp < rootq:
            self.root[rootq] = rootp
        else:
            self.root[rootp] = rootq


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UF()
        for i in range(len(s1)):
            uf.union(s1[i], s2[i])
        
        res = ''
        for i in range(len(baseStr)):
            res += uf.find(baseStr[i])
        
        return res
