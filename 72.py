# Edit Distance
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/84935585
# https://labuladong.github.io/algo/di-er-zhan-a01c6/zi-xu-lie--6bc09/jing-dian--f3f6e/
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


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        memo = [[-1] * n2 for _ in range(n1)]

        def dp(word1, i, word2, j):
            if i == -1: return j + 1
            if j == -1: return i + 1
            if memo[i][j] != -1:
                return memo[i][j]
        
            if word1[i] == word2[j]:
                memo[i][j] = dp(word1, i-1, word2, j-1)
            else:
                memo[i][j] = min(dp(word1, i-1, word2, j), dp(word1, i, word2, j-1), dp(word1, i-1, word2, j-1)) + 1
            return memo[i][j]


        return dp(word1, n1-1, word2, n2-1)
      