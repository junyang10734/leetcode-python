# 712. Minimum ASCII Delete Sum for Two Strings
# Compare with 583, 1143
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/79822689
# runtime: faster than 95.53%
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return sum(map(ord, s1+s2)) - dp[-1][-1] * 2


# 带 memory 的 DP
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        memo = [[-1] * n for _ in range(m)]

        def dp(s1, i, s2, j):
            res = 0
            if i == len(s1):
                while j < len(s2):
                    res += ord(s2[j])
                    j += 1
                return res
            
            if j == len(s2):
                while i < len(s1):
                    res += ord(s1[i])
                    i += 1
                return res
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            if s1[i] == s2[j]:
                memo[i][j] = dp(s1, i+1, s2, j+1)
            else:
                memo[i][j] = min(dp(s1, i+1, s2, j) + ord(s1[i]), dp(s1, i, s2, j+1) + ord(s2[j]))
            
            return memo[i][j]
        
        return dp(s1, 0, s2, 0)