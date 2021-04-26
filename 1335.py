# 1335. Minimum Difficulty of a Job Schedule
# DP


# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/924611/DFS-greater-DP-Progression-with-Explanation-O(n3d)O(nd)
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        if d > N:
            #not enough tasks to split into each day
            return -1
        dp = [[float("inf")]*d for _ in range(N)]
        #fill out first column based on max(jobDiffculty[0:i])
        dp[0][0] = jobDifficulty[0]
        for i in range(1,N):
            dp[i][0] = max(dp[i-1][0],jobDifficulty[i])

        #fill out dp
        for i in range(1,N):
            for j in range(1,min(i+1,d)):
                #i+1 is the crossed out boxes since there's not enough tasks to break up into multiple days
                #d is the right end of the dp grid
                for k in range(i):
                    #this is where we take terms that are calculated already on k,j-1 tile
                    dp[i][j] = min(dp[i][j], dp[k][j-1] + max(jobDifficulty[k+1:i+1]))
                    #Note that min() is tring to get the lowest difficulty among the k possible break-ups of #tasks=i,#days=j
        return dp[-1][-1]

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

                    