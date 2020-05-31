# Shortest Unsorted Continuous Subarray
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/79254454
# runtime: faster than 67.72%
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        if new_nums == nums:
            return 0
        
        difference = [i for i in range(len(nums)) if nums[i] != new_nums[i]]
        l = min(difference)
        r = max(difference)
        
        return r-l+1