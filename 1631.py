# 1631. Path With Minimum Effort
# Dijkstra's alg

# https://leetcode.com/problems/path-with-minimum-effort/solutions/909017/java-python-dijikstra-binary-search-clean-concise/
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        distance = [[math.inf] * n for _ in range(m)]
        distance[0][0] = 0

        heap = [(0, 0, 0)] # distance, row, col
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            d, r, c = heapq.heappop(heap)
            if d > distance[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return d
            
            for x,y in dirs:
                nr, nc = r+x, c+y
                if 0 <= nr < m and 0 <= nc < n:
                    newD = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if distance[nr][nc] > newD:
                        distance[nr][nc] = newD
                        heapq.heappush(heap, (newD, nr, nc))
