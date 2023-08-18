# 714. Best Time to Buy and Sell Stock with Transaction Fee
# 股票问题 121，122，123，188，309，714
# DP

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/
# running time: faster than 62.43%
class Solution1:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash


# labuladong
# runtime: faster than 49.09%
# compare with 122
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
# 解释：相当于买入股票的价格升高了。
# 在第一个式子里减也是一样的，相当于卖出股票的价格减小了。
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0], dp[0][1] = 0, -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        
        return dp[-1][0]
# 空间压缩
class Solution2:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp_0, dp_1 = 0, float('-inf')
        for i in range(len(prices)):
            temp = dp_0
            dp_0 = max(dp_0, dp_1+prices[i])
            dp_1 = max(dp_1, temp-prices[i]-fee)
        return dp_0