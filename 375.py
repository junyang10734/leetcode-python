# 375. Guess Number Higher or Lower II
# DP / Recursion

# https://www.hrwhisper.me/leetcode-guess-number-higher-lower-ii/
# DP
# running time: faster than 10.61%
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        return self.solve(dp, 1, n)
    
    
    def solve(self, dp, l, r):
        if l >= r:
            return 0
        if dp[l][r]:
            return dp[l][r]
        dp[l][r] = min(i + max(self.solve(dp, l, i-1), self.solve(dp, i+1, r)) for i in range(l, r+1))
        return dp[l][r]


# Recursive
# running time: faster than 73.99%
class Solution2:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1, 0, -1):
            for j in range(i+1, n+1):
                dp[i][j] = min(a + max(dp[i][a-1], dp[a+1][j]) for a in range(i,j))

        return dp[1][n]
    