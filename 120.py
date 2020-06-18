# Triangle
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/82883187
# runtime: faster than 90.10%
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1]
        for k in range(n-2, -1, -1):
            for i in range(k+1):
                dp[i] = min(dp[i], dp[i+1]) + triangle[k][i]
        return dp[0]
