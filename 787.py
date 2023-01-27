# Cheapest Flights Within K Stops
# Graph


# https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/267200/python-dijkstra/?orderBy=most_votes
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, k+1)]
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= k:
                continue
            vis[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w+dw, y, k-1))
        return -1


# https://blog.csdn.net/fuxuemingzhu/article/details/83307822

# DFS
# runtime: faster than 7.93% 
class Solution1:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for u,v,e in flights:
            graph[u][v] = e
        visited = [0] * n
        ans = [float('inf')]
        self.dfs(graph, src, dst, K+1, 0, visited, ans)
        
        return -1 if ans[0] == float('inf') else ans[0]

    def dfs(self, graph, src, dst, k, cost, visited, ans):
        if src == dst:
            ans[0] = cost
        if k == 0:
            return 
        for v,e in graph[src].items():
            if visited[v]: 
                continue
            if cost + e > ans[0]:
                continue
            visited[v] = 1
            self.dfs(graph, v, dst, k-1, cost+e, visited, ans)
            visited[v] = 0


# BFS
# runtime: faster than 39.28%
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for u,v,e in flights:
            graph[u][v] = e
        ans = float('inf')
        que = collections.deque()
        que.append((src,0))
        step = 0
        
        while que:
            size = len(que)
            for i in range(size):
                cur, cost = que.popleft()
                if cur == dst:
                    ans = min(ans, cost)
                for v, w in graph[cur].items():
                    if cost + w > ans:
                        continue
                    que.append((v, cost+w))
            if step > K: 
                break
            step += 1
        
        return -1 if ans == float('inf') else ans



# http://bookshadow.com/weblog/2018/02/18/leetcode-cheapest-flights-within-k-stops/
# heap
# runtime: faster than 62.24% 
class Solution3:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, K + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1

# DP
# https://labuladong.github.io/algo/di-er-zhan-a01c6/yong-dong--63ceb/lv-you-she-2b4f3/
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        indegree = collections.defaultdict(list)
        for s,t,p in flights:
            indegree[t].append((s, p))

        # 从 src 出发，k 步之内到达 s 的最短路径权重
        def dp(s, step):
            if s == src:
                return 0
            if step == 0:
                return -1
            
            res = math.inf
            if len(indegree[s]) > 0:
                for source, cost in indegree[s]:
                    # print(source)
                    subPath = dp(source, step-1)
                    if subPath != -1:
                        res = min(res, subPath + cost)

            return -1 if res == math.inf else res

        return dp(dst, k+1)