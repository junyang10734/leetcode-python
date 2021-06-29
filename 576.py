# 576. Out of Boundary Paths
# DP / Recursion with Memoization

# https://leetcode.com/problems/out-of-boundary-paths/solution/

# Recursion with Memoization
# runtime: O(mnN)
class Solution1:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = [[[-1] * (maxMove + 1) for i in range(n)] for j in range(m)]
        
        def helper(m, n, move, i, j):
            if i == m or j == n or i < 0 or j < 0:
                return 1
            if move == 0:
                return 0
            if memo[i][j][move] >= 0:
                return memo[i][j][move]
            
            memo[i][j][move] = (helper(m, n, move-1, i-1, j) + helper(m, n, move-1, i+1, j) + helper(m, n, move-1, i, j-1) + helper(m, n, move-1, i, j+1)) % (10 ** 9 + 7)
            return memo[i][j][move]
        
        return helper(m, n, maxMove, startRow, startColumn)


# DP
# runtime: O(Nmn)
class Solution2:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M = 10 ** 9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        count = 0
        
        for move in range(maxMove):
            tmp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m-1:
                        count = (count + dp[i][j]) % M
                    if j == n-1:
                        count = (count + dp[i][j]) % M
                    if i == 0:
                        count = (count + dp[i][j]) % M
                    if j == 0:
                        count = (count + dp[i][j]) % M
                    tmp[i][j] = ((dp[i-1][j] if i > 0 else 0) + (dp[i+1][j] if i < m-1 else 0) + (dp[i][j-1] if j > 0 else 0) + (dp[i][j+1] if j < n-1 else 0)) % M
            dp = tmp
    
        return count