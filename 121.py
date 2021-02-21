# 121. Best Time to Buy and Sell Stock
# DP
# 股票问题 121，122，123，188，309，714

# 动态规划
# minP 记录最低股价
# 第i天的最大收益为下面两者中的最大值：
# 第i-1天的最大收益
# 第i天的股价 - minP
# Space: O(n)
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        profits = [0] * len(prices)
        minP = prices[0]
        for i in range(len(prices)):
            if i!=0:
                profits[i] = max(profits[i-1], prices[i] - minP )
                minP = min(minP, prices[i])
        
        return max(profits) 


# Space: O(1)
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        minP, maxProfits = prices[0], 0
        for p in prices:
            minP = min(minP, p)
            maxProfits = max(maxProfits, p - minP)
        return maxProfits


# labuladong 
# DP
# runtime: faster than 6.32%
# dp[i][k][0 or 1]
# 0 <= i <= n-1, 1 <= k <= K
# n 为天数，大 K 为最多交易数
# base case：
# dp[-1][k][0] = dp[i][0][0] = 0
# dp[-1][k][1] = dp[i][0][1] = -infinity
# 状态转移方程：
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0]*2 for _ in range(N+1)]
        
        for i in range(N):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
                dp[i][1] = max(dp[i-1][1], -prices[i])
        
        return dp[N-1][0]


# labuladong
# DP, less space
# runtime: faster than 18.73%
class Solution4:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(N):
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        
        return dp_i_0