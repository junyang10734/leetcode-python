# Longest Common Subsequence
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