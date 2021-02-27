# 1335. Minimum Difficulty of a Job Schedule
# DP

# https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-1335-minimum-difficulty-of-a-job-schedule/
# https://walkccc.me/LeetCode/problems/1335/
# runtime: faster than 52.26%
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        elif n == d:
            return sum(jobDifficulty)
        
        dp = [[inf]*(d+1) for _ in range(n+1)]
        dp[0][0] = 0

        for i in range(1, n+1):
            for j in range(1, d+1):
                maxD = 0
                for k in range(i-1, j-2, -1):
                    maxD = max(maxD, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], dp[k][j-1] + maxD)
        
        return dp[n][d]


class Solution2:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        elif n == d:
            return sum(jobDifficulty)
        
        dp = [[inf]*(n+1) for _ in range(d+1)]
        dp[0][0] = 0

        for i in range(1, d+1):
            for j in range(1, n+1):
                maxD = 0
                for k in range(j-1, i-2, -1):
                    maxD = max(maxD, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], maxD+dp[i-1][k])
        
        return dp[d][n]
                    