# 2421. Number of Good Paths
# Union Find

# https://leetcode.com/problems/number-of-good-paths/solutions/2620529/python-explanation-with-picture-dsu/?orderBy=most_votes
class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1 for i in range(n)]
    
    def find(self, p):
        while p != self.root[p]:
            self.root[p] = self.root[self.root[p]]
            p = self.root[p]
        return p 


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        res = n = len(vals)
        uf = UnionFind(n)

        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        count = collections.defaultdict(dict)
        for i, v in enumerate(vals):
            count[i][v] = 1
          
        for v, cur in sorted([v, i] for i,v in enumerate(vals)):
            for nxt in graph[cur]:
                root_nxt,root_cur = uf.find(nxt), uf.find(cur)
                if vals[nxt] <= v and root_cur != root_nxt:
                    uf.root[root_cur] = root_nxt
                    res += count[root_cur][v] * count[root_nxt].get(v, 0)
                    count[root_nxt][v] = count[root_nxt].get(v, 0) + count[root_cur][v]

        
        return res


