# 1312. Minimum Insertion Steps to Make a String Palindrome
# DP

# labuladong
# runtime: faster than 93.71%
class Solution1:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        
        return dp[0][n-1]


# Same with Solution1, less space
# runtime: faster than 98.48%
class Solution2:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        
        for i in range(n-2, -1, -1):
            pre = 0
            for j in range(i+1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j], dp[j-1]) + 1
                pre = temp
        
        return dp[n-1]