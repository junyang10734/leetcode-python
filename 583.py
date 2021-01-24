# 583. Delete Operation for Two Strings
# Compare with 516, 1143
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/79821305
# runtime: faster than 84.15% 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        lcs = dp[-1][-1]
        return (n1 - lcs) + (n2 - lcs)