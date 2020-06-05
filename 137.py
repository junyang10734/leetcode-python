# Single Number II
# Array

# runtime: faster than 62.62%
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)-3, 3):
            if nums[i] != nums[i+2]:
                return nums[i]
        
        return nums[-1]