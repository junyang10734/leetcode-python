# 802. Find Eventual Safe States
# compare: 207, 210
# Graph / DFS

# https://blog.csdn.net/fuxuemingzhu/articler/details/82749341
# running time: faster than 96.89%
class Solution1:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0] * len(graph)
        
        def dfs(g, i, c):
            if c[i] != 0:
                return c[i] == 1
            c[i] = 2
            for e in g[i]:
                if not dfs(g, e, c):
                    return False
            c[i] = 1
            return True
        
        
        res = []
        for i in range(len(graph)):
            if dfs(graph, i, color):
                res.append(i)

        res.sort()
        return res