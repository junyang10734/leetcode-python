# 256. Paint House
# DP

# runtime: O(m*n)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for i in range(1, len(costs)):
            for j in range(len(costs[0])):
                costs[i][j] += min(costs[i-1][:j] + costs[i-1][j+1:])
        
        return min(costs[-1])