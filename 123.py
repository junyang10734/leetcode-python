# 123. Best Time to Buy and Sell Stock III
# 股票问题 121，122，123，188，309，714


# labuladong
# DP
# runtime: faster than 5.41%
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        dp = [[[0]* 2 for j in range(k+1)] for i in range(len(prices))]
        
        for i in range(len(prices)):
            dp[i][0][0], dp[i][0][1] = 0, float('-inf')
            
        for i in range(len(prices)):
            for k in range(2, 0, -1):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                else:
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        return dp[len(prices)-1][2][0]


# dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
# dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
# dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
# dp[i][1][1] = max(dp[i-1][1][1], -prices[i])
# runtime: faster than 71.63%
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i10, dp_i20 = 0, 0
        dp_i11, dp_i21 = float('-inf'), float('-inf')
        for p in prices:
            dp_i20 = max(dp_i20, dp_i21 + p)
            dp_i21 = max(dp_i21, dp_i10 - p)
            dp_i10 = max(dp_i10, dp_i11 + p)
            dp_i11 = max(dp_i11, -p)
        
        return dp_i20