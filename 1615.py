# 1615. Maximal Network Rank
# Graph

# https://leetcode.com/problems/maximal-network-rank/editorial/
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxRank = 0
        adj = collections.defaultdict(set)

        for a, b in roads:
            adj[a].add(b)
            adj[b].add(a)
        
        for node1 in range(n):
            for node2 in range(node1+1, n):
                currentRank = len(adj[node1]) + len(adj[node2])
                if node2 in adj[node1]:
                    currentRank -= 1
                maxRank = max(maxRank, currentRank)
        
        return maxRank