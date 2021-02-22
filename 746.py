# 746. Min Cost Climbing Stairs
# DP

# runtime: faster than 48.81%
class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]

        return min(dp[i-1], dp[i])


# less space
# runtime: faster than 90.99%
class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = cost[0], cost[1]

        for i in range(2, len(cost)):
            res = min(first, second) + cost[i]
            first = second
            second = res

        return min(first, second)