# 486. Predict the Winner
# DP
# compare with 877

# https://labuladong.github.io/algo/di-er-zhan-a01c6/yong-dong--63ceb/jing-dian--ff413/
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[[0,0] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i][0] = nums[i]

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                left = nums[i] + dp[i+1][j][1]
                right = nums[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]
        
        return dp[0][n-1][0] >= dp[0][n-1][1]