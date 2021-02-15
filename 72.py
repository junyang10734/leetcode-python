# Edit Distance
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/84935585
# https://labuladong.github.io/algo/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E7%BC%96%E8%BE%91%E8%B7%9D%E7%A6%BB.html
# runtime: faster than 70.79%
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1, L2 = len(word1), len(word2)
        dp = [[0] * (L2 + 1) for _ in range(L1 + 1)]
        for i in range(L1 + 1):
            dp[i][0] = i
        for j in range(L2 + 1):
            dp[0][j] = j
        for i in range(1, L1 + 1):
            for j in range(1, L2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[L1][L2]
