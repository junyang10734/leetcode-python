# 1443. Minimum Time to Collect All Apples in a Tree
# DFS

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(v, parent):
            if len(graph[v]) == 0:
                return 0

            totalTime, childrenTime = 0, 0
            for child in graph[v]:
                if child == parent:
                    continue
                childrenTime = dfs(child, v)
                if childrenTime > 0 or hasApple[child]:
                    totalTime += childrenTime + 2

            return totalTime

        return dfs(0, -1)
