# 1135. Connecting Cities With Minimum Cost
# Union-Find + 最小生成树之 Kruskal 算法 / Prim 算法

# Kruskal 算法
class DSU:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n
        self.count = n
    
    def find(self, p):
        while self.root[p] != p:
            self.root[p] = self.root[self.root[p]]
            p = self.root[p]
        return p
    
    def union(self, p, q):
        rootp, rootq = self.find(p), self.find(q)
        if rootp == rootq:
            return
        
        if self.rank[rootp] <= self.rank[rootq]:
            self.root[rootp] = rootq
            self.rank[rootq] += self.rank[rootp]
        else:
            self.root[rootq] = rootp
            self.rank[rootp] += self.rank[rootq]

        self.count -= 1

    def getCount(self):
        return self.count

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x:x[2])
        dsu = DSU(n+1)
        res = 0

        for x,y,cost in connections:
            if dsu.find(x) == dsu.find(y):
                continue
            res += cost
            dsu.union(x, y)
            
        # 判断最后的连通分量个数（label从1开始）, 若连通分量数为2(0自己有一个独立的），则表示所有node都联通了
        return res if dsu.getCount() == 2 else -1


# Prim 算法
# https://labuladong.github.io/algo/2/22/55/
class Solution2:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for x,y,cost in connections:
            # the lable starts from 1, but our Prim class starts from 0
            graph[x-1].append((cost, y-1))
            graph[y-1].append((cost, x-1))

        heap = [(0, 0)]
        mst = set()
        res = 0
        while heap:
            cost, node = heapq.heappop(heap)
            if node not in mst:
                mst.add(node)
                res += cost
                for nx in graph[node]:
                    heapq.heappush(heap, nx)
        
        return res if len(mst) == n else -1