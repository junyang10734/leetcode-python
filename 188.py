# 188. Best Time to Buy and Sell Stock IV
# 股票问题 121，122，123，188，309，714

# labuladong
# 122 + 123
# 一次交易由买入和卖出构成，至少需要两天，所以说有效的限制 k 应该不超过 n/2
# 如果超过，就没有约束作用了，相当于 k = +infinity，即 122题
# 如果没有超过，则为 k 值可变的123题
# runtime: faster than 26.71%
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k > n/2:
            dp_0, dp_1 = 0, float('-inf')
            for i in range(len(prices)):
                temp = dp_0
                dp_0 = max(dp_0, dp_1+prices[i])
                dp_1 = max(dp_1, temp-prices[i])
            return dp_0
        else:
            dp = [[[0]* 2 for j in range(k+1)] for i in range(n)]
        
            for i in range(len(prices)):
                dp[i][0][0], dp[i][0][1] = 0, float('-inf')

            for i in range(len(prices)):
                for _k in range(k, 0, -1):
                    if i == 0:
                        dp[i][_k][0] = 0
                        dp[i][_k][1] = -prices[i]
                    else:
                        dp[i][_k][0] = max(dp[i-1][_k][0], dp[i-1][_k][1] + prices[i])
                        dp[i][_k][1] = max(dp[i-1][_k][1], dp[i-1][_k-1][0] - prices[i])

            return dp[n-1][k][0]
