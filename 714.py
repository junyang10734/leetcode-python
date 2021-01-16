# 714. Best Time to Buy and Sell Stock with Transaction Fee
# DP
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/

# running time: faster than 62.43%
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash