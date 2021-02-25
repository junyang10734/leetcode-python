# 300. Longest Increasing Subsequence
# compare: 673, 1048
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/79820919
# runtime: faster than 16.23%
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        dp = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)