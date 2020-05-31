# Target Sum
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/80484450
# runtime: faster than 79.06%
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [ collections.defaultdict(int) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        
        for k, v in enumerate(nums):
            for s,cnt in dp[k].items():
                dp[k+1][s+v] += cnt
                dp[k+1][s-v] += cnt
        
        return dp[len(nums)][S]
