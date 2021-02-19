# 877. Stone Game
# DP

# labuladong
# runtime: faster than 40.08%
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[(0,0)] * (n+1) for _ in range(n+1)]

        
        for l in range(2, n+1):
            for i in range(0, n):
                j = l + i - 1
                if j < n:
                    left = piles[i] + dp[i+1][j][1]
                    right = piles[j] + dp[i][j-1][1]
                
                    if left > right:
                        dp[i][j] = (left, dp[i+1][j][0])
                    else:
                        dp[i][j] = (right, dp[i][j-1][0])
        
        res = dp[0][n-1]
        return res[0] > res[1]