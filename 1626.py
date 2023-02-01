# 1626. Best Team With No Conflicts
# DP

# https://leetcode.com/problems/best-team-with-no-conflicts/solutions/2886659/best-team-with-no-conflicts/
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        arr = [[ages[i], scores[i]] for i in range(n)]
        arr.sort(key=lambda x: (x[0], x[1]))
        
        dp = [arr[i][1] for i in range(n)]
        res = max(dp)
        for i in range(n):
            for j in range(i-1, -1, -1):
                if arr[i][1] >= arr[j][1]:
                    dp[i] = max(dp[i], dp[j] + arr[i][1])
            res = max(res, dp[i])

        return res