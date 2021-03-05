# 1192. Critical Connections in a Network
# DFS

# https://leetcode.com/problems/critical-connections-in-a-network/discuss/1082197/Python-DFS
# runtime: faster than 68.51%
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for i, j in connections:
            d[i].append(j)
            d[j].append(i)
            
        low, res = {}, []
        
        def dfs(node, parent=None):
            if node in low:
                return low[node]
            
            cur = low[node] = len(low)
            for neigh in d[node]:
                if neigh == parent:
                    continue
                low[node] = min(low[node], dfs(neigh, node))
            
            if cur == low[node] and parent is not None:
                res.append([parent, node])
            
            return low[node]
        
        dfs(0)
        return res
