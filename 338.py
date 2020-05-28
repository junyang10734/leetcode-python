# Counting Bits
# DP / Bit Manipulation

# https://blog.csdn.net/fuxuemingzhu/article/details/70806676
# runtime: faster than 75.93%
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num+1)
        
        for i in range(1, num+1):
            dp[i] = dp[i//2] + i%2
        
        return dp     