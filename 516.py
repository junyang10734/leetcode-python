# 516. Longest Palindromic Subsequence
# Compare with 1143, 647, 583
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/79572746
# https://zhenyu0519.github.io/2020/03/01/lc516/
# runtime: faster than 75.76% 
# 1. i > j，dp[i][j] = 0； 
# 2. i == j，dp[i][j] = 1； 
# 3. i < j且s[i] == s[j]，dp[i][j] = dp[i + 1][j - 1] + 2； 
# 4. i < j且s[i]！= s[j]，dp[i][j] = max(dp[i + 1][j]，dp[i][j - 1])；
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]