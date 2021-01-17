# 309. Best Time to Buy and Sell Stock with Cooldown
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