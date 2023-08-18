# 2369. Check if There is a Valid Partition For The Array
# DP

# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/editorial/
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [True] + [False] * n

        for i in range(n):
            idx = i + 1

            if i > 0 and nums[i] == nums[i-1]:
                dp[idx] |= dp[idx - 2]
            if i > 1 and nums[i] == nums[i-1] == nums[i-2]:
                dp[idx] |= dp[idx - 3]
            if i > 1 and nums[i] == nums[i-1] + 1 == nums[i-2] + 2:
                dp[idx] |= dp[idx - 3]
            
        return dp[-1]