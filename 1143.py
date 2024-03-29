# Longest Common Subsequence
# Compare with 516, 583, 712
# DP

# https://leetcode.com/problems/longest-common-subsequence/discuss/381651/Python-2d-dp-Onm
# runtime: faster than 79.61%
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [ [0]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i][j] = (dp[i-1][j-1] if i>0 and j>0 else 0) + 1
                else:
                    dp[i][j] = max(dp[i-1][j] if i>0 else 0, dp[i][j-1] if j>0 else 0)
        
        return dp[-1][-1]


# 带 memory 的 dp
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = [[-1] * n for _ in range(m)]

        def dp(text1, i, text2, j):
            if i == len(text1) or j == len(text2):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            
            if text1[i] == text2[j]:
                memo[i][j] = dp(text1, i+1, text2, j+1) + 1
            else:
                memo[i][j] = max(dp(text1, i+1, text2, j), dp(text1, i, text2, j+1))
            
            return memo[i][j]
        
        return dp(text1, 0, text2, 0)