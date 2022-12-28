# 1584. Min Cost to Connect All Points
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

class Solution1:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n-1):
            for j in range(i+1, n):
                x = abs(points[i][0] - points[j][0])
                y = abs(points[i][1] - points[j][1])
                edges.append((i, j, x+y))
        
        edges.sort(key=lambda x:x[2])
        dsu = DSU(n)
        res = 0
        for x,y,distance in edges:
            if dsu.find(x) == dsu.find(y):
                continue
            res += distance
            dsu.union(x, y)
        return res


# Prim 算法
# https://labuladong.github.io/algo/2/22/55/
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = collections.defaultdict(list)
        for i in range(n-1):
            for j in range(i+1, n):
                graph[i].append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), j))
                graph[j].append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i))
        
        heap = [(0, 0)]
        mst = set()
        res = 0
        while heap:
            distance, node = heapq.heappop(heap)
            if node in mst:
                continue
            mst.add(node)
            res += distance
            if len(mst) == n:
                return res
            for nx in graph[node]:
                heapq.heappush(heap, nx)
            