# 1690. Stone Game VII
# DP

# https://leetcode.com/problems/stone-game-vii/solution/
# Approach 4: Bottom Up Dynamic Programming - Tabulation
# runtime: O(n**2)
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        preSum = [0] * (n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + stones[i]
        
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n+1):
            for start in range(n - length + 1):
                end = start + length - 1
                scoreRemoveFirst = preSum[end+1] - preSum[start+1]
                socreRemoveLast = preSum[end] - preSum[start]
                dp[start][end] = max(scoreRemoveFirst - dp[start+1][end], socreRemoveLast - dp[start][end-1])
        
        return dp[0][-1]