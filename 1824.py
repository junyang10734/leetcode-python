# 1824. Minimum Sideway Jumps
# DP

# https://leetcode.com/problems/minimum-sideway-jumps/discuss/1152416/Python3-DP-solution
# runtime: O(n)
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[float('inf')]*3 for _ in range(n)]
        dp[0] = [1, 0, 1]
        
        for i in range(1, n):
            for j in range(3):
                if obstacles[i] != j+1:
                    dp[i][j] = dp[i-1][j]
            cur_min = min(dp[i])
            for j in range(3):
                if obstacles[i] != j+1:
                    dp[i][j] = min(dp[i][j], cur_min + 1)
        return min(dp[-1])