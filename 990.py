# 990. Satisfiability of Equality Equations
# Union-Find

# runtime: faster than 53.55%
# https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/1062535/Python-DSU-method
class UF:
    def __init__(self):
        self.parent = list(range(30))
        self.size = [1 for _ in range(30)]
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]  
        return x
    
    def union(self, p, q):
        rootp, rootq = self.find(p), self.find(q)
        if rootp == rootq:
            return
        if self.size[rootp] > self.size[rootq]:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        else:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF()
        records = []
        initial = ord('a')
        for eq in equations:
            if eq[1] == '=':
                uf.union(ord(eq[0]) - initial, ord(eq[-1]) - initial)
            else:
                records.append(eq)
                
        for record in records:
            if uf.find(ord(record[0])-initial) == uf.find(ord(record[-1])-initial):
                return False
        
        return True

                