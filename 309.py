# 309. Best Time to Buy and Sell Stock with Cooldown
# 股票问题 121，122，123，188，309，714
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/82656899
# running time: faster than 87.42% 
# Space: O(n)
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        sell, hold = [0]*len(prices), [0]*len(prices)
        hold[0] = -prices[0]
        
        for i in range(1, len(prices)):
            sell[i] = max(hold[i-1]+prices[i], sell[i-1])
            hold[i] = max((sell[i-2] if i>=2 else 0)-prices[i], hold[i-1])
        
        return sell[-1]


# running time: faster than 69.96%
# Space: O(1)
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        prev_sell = 0
        curr_sell = 0
        hold = -prices[0]
        
        for i in range(1, len(prices)):
            temp = curr_sell
            curr_sell = max(hold+prices[i], curr_sell)
            hold = max((prev_sell if i>=2 else 0)-prices[i], hold)
            prev_sell = temp
        return curr_sell


# labuladong
# runtime: faster than 88.87%
# compare with 122
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
# 解释：第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            if i == 1:
                dp[1][0] = max(dp[0][0], dp[0][1] + prices[i])
                dp[1][1] = max(dp[0][1], -prices[1])
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        return dp[-1][0]
# 空间压缩
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i0, dp_i1 = 0, float('-inf')
        dp_pre0 = 0
        for i in range(len(prices)):
            temp = dp_i0
            dp_i0 = max(dp_i0, dp_i1 + prices[i])
            dp_i1 = max(dp_i1, dp_pre0 - prices[i])
            dp_pre0 = temp
        
        return dp_i0
