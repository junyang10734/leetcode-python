# 动态规划
# dp[i]表示包含nums[i]的最大子数组和
# 迭代公式： dp[i] = max(nums[i], nums[i]+dp[i-1])
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        if len(nums) == 1:
            return sum
        else:
            dp = [0]*len(nums)
            dp[0] = nums[0]
            for i in range(1,len(nums)):
                dp[i] = max(nums[i], nums[i]+dp[i-1])

            return max(dp)