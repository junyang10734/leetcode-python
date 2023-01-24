# 651. 4 Keys Keyboard
# DP

# https://labuladong.github.io/algo/di-er-zhan-a01c6/yong-dong--63ceb/jing-dian--efbd9/
class Solution:
    def maxA(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1
            for j in range(2, i-1):
                dp[i] = max(dp[i], dp[j-2] * (i - j + 1))
        return dp[-1]
