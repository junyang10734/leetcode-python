# 动态规划
# minP 记录最低股价
# 第i天的最大收益为下面两者中的最大值：
# 第i-1天的最大收益
# 第i天的股价 - minP
class Solution:
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