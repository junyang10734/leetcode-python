# 163. Missing Ranges
# Array

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[lower, upper]]

        res = []
        if lower < nums[0]:
            res.append([lower, nums[0]-1])

        for i in range(n-1):
            if nums[i+1] - nums[i] <= 1:
                continue
            res.append([nums[i]+1, nums[i+1]-1])
        
        if upper > nums[n-1]:
            res.append([nums[n-1]+1, upper])
        
        return res
