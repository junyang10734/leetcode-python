# Best Time to Buy and Sell Stock II
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