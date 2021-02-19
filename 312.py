# 312. Burst Balloons
# DP

# labuladong
# runtime: faster than 36.82%
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        points = []
        points.append(1)
        for num in nums:
            points.append(num)
        points.append(1)
        
        dp = [[0]*(n+2) for _ in range(n+2)]
        for i in range(n, -1, -1):
            for j in range(i+1, n+2):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + points[i]*points[j]*points[k])
    
        return dp[0][n+1]