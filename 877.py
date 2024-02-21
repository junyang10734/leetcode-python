# 877. Stone Game
# DP / Game Theory
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
    

# DP
# https://leetcode.com/problems/stone-game/solutions/154610/dp-or-just-return-true/
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])
        return dp[0][-1] > 0


# Game Theory
# https://labuladong.github.io/algo/di-san-zha-24031/shu-xue-yu-659f1/yi-xing-da-1d528/
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True