# 743. Network Delay Time
# Dijkstra's alg


# https://leetcode.com/problems/network-delay-time/solution/

# DFS
# running time: TLE
class Solution1:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        d = {node: float('inf') for node in range(1, N+1)}
         
        def dfs(node, distance):
            if distance >= d[node]:
                return
            d[node] = distance
            for nei, time in sorted(graph[node]):
                dfs(nei, distance + time)
            
        dfs(K, 0)
        ans = max(d.values())
        return ans if ans < float('inf') else -1


# Dijkstra's alg
# Basic Implementation
# running time: faster than 82.58% 
class Solution2:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        dist = {node: float('inf') for node in range(1, N+1)}
        seen = [False] * (N+1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_node = i
                    cand_dist = dist[i]
                    
            if cand_node < 0:
                break
            seen[cand_node] = True
            for nei, distance in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + distance)
                
        ans = max(dist.values())
        return ans if ans < float('inf') else -1


# Dijkstra's alg
# Heap Implementation
# running time: faster than 61.07%
class Solution3:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        pq = [(0,K)]
        dist = {}
        
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = d
            
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))
        
        return max(dist.values()) if len(dist) == N else -1