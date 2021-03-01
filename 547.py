# 547. Number of Provinces
# DFS

# runtime: faster than 32.49%
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        def dfs(city):
            for nei, connected in enumerate(isConnected[city]):
                if connected and nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        res = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res
