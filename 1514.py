# 1514. Path with Maximum Probability
# Dijkstra's alg

# https://leetcode.com/problems/path-with-maximum-probability/solutions/731767/java-python-3-2-codes-bellman-ford-and-dijkstra-s-algorithm-w-brief-explanation-and-analysis/
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])

        p = [0] * n
        p[start] = 1
        heap = [(-p[start], start)]
        while heap:
            prob, node = heapq.heappop(heap)
            if node == end:
                return -prob

            for nx, nxProb in graph[node]:
                if -prob * nxProb > p[nx]:
                    p[nx] = -prob * nxProb
                    heapq.heappush(heap, (-p[nx], nx))
        
        return 0.0