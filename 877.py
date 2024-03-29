# 877. Stone Game
# DP
# compare with 486

# labuladong
# runtime: faster than 40.08%
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[[0,0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i][0] = piles[i]

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]
        
        return dp[0][n-1][0] > dp[0][n-1][1]