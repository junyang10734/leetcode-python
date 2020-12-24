# 837. New 21 Game
# DP

# https://www.cnblogs.com/grandyang/p/10386525.html
# https://blog.csdn.net/fuxuemingzhu/article/details/83615241
# running time: faster than 66.18%
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1
        
        dp = [1.0] + [0] * N
        tsum = 1.0
        
        for i in range(1, N+1):
            dp[i] = tsum / W
            if i < K:
                tsum += dp[i]
            if 0 <= i - W < K:
                tsum -= dp[i-W]
        
        return sum(dp[K:])
