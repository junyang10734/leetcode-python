# 839. Similar String Groups
# Graph / Union-Find

# https://leetcode.com/problems/similar-string-groups/solution/
# runtime: faster than 33.24% 
class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]
        self.count = n
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        rootp, rootq = self.find(p), self.find(q)
        if rootp == rootq:
            return 
        if self.size[rootp] >= self.size[rootq]:
            self.parent[rootq] = self.parent[rootp]
            self.size[rootp] += self.size[rootq]
        else:
            self.parent[rootp] = self.parent[rootq]
            self.size[rootq] += self.size[rootp]
        self.count -= 1

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n, w = len(strs), len(strs[0])
        uf = UF(n)
        
        for (i1, word1), (i2, word2) in itertools.combinations(enumerate(strs), 2):
            if self.isSimilar(word1, word2):
                uf.union(i1, i2)

        return uf.count
    
    def isSimilar(self, word1, word2):
        diff = 0
        for x,y in zip(word1, word2):
            if x != y:
                diff += 1
        return diff <= 2