# 1480. Running Sum of 1d Array
# Array

# runtime: O(n)
# space: O(1)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums