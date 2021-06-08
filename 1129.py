# 1129. Shortest Path with Alternating Colors
# Graph

# BFS
# https://leetcode.com/problems/shortest-path-with-alternating-colors/discuss/339964/JavaPython-BFS
# runtime: faster than 84.30%
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        G = [[[],[]] for i in range(n)]
        for i,j in red_edges:
            G[i][0].append(j)
        for i,j in blue_edges:
            G[i][1].append(j)
        
        res = [[0, 0]] + [[n*2, n*2] for i in range(n-1)]
        bfs = [[0, 0], [0, 1]]
        for i,c in bfs:
            for j in G[i][c]:
                if res[j][c] == n*2:
                    res[j][c] = res[i][1-c] + 1
                    bfs.append([j, 1-c])
        
        return [x if x < n*2 else -1 for x in map(min, res)]