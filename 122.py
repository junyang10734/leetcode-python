# Best Time to Buy and Sell Stock II
# 股票问题 121，122，123，188，309，714


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profits = 0
        # flag==0,we've bought stocks, we need to sell them
        # flag==1,we've sell stocks, we need to buy them
        flag = 0  
        prices.append(0)
        for i in range(len(prices)-1):
            if flag == 0:
                if prices[i] < prices[i+1]:
                    buy = prices[i]
                    flag = 1
            else:
                if prices[i] > prices[i+1]:
                    sell = prices[i]
                    profits = profits + prices[i] - buy
                    flag = 0
        
        return profits


# https://blog.csdn.net/fuxuemingzhu/article/details/70258549
# running time: faster than 99.50%
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profits = profits + prices[i] - prices[i-1]
        return profits


# labuladong
# DP
# runtime: faster than 50.09%
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
        dp_0, dp_1 = 0, float('-inf')
        for i in range(len(prices)):
            temp = dp_0
            dp_0 = max(dp_0, dp_1+prices[i])
            dp_1 = max(dp_1, temp-prices[i])
        return dp_0