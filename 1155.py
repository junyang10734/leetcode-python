# 1155. Number of Dice Rolls With Target Sum
# DP


# https://zhenyu0519.github.io/2020/03/04/lc1155/
# running time: faster than 87.00%
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0]*(target+1) for _ in range(d+1)]
        dp[0][0] = 1
        
        if target < 1 or target > d*f:
            return 0
        
        for i in range(1, d+1):
            for j in range(1, f+1):
                for k in range(j, target+1):
                    dp[i][k] += dp[i-1][k-j]
        
        return dp[-1][-1] % (10**9+7)
