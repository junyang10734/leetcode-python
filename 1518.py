# 1518. Water Bottles
# Math

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            div, remainder = divmod(numBottles, numExchange)
            res += div
            numBottles = div + remainder
        return res