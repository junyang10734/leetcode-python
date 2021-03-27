# 487. Max Consecutive Ones II
# Array / Sliding Window

# https://leetcode.com/problems/max-consecutive-ones-ii/solution/
# runtime: faster than 32.34%
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        l, r = 0, 0
        num_zeros = 0
        
        while r < len(nums):
            if nums[r] == 0:
                num_zeros += 1
            while num_zeros == 2:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            longest = max(longest, r-l+1)
            r += 1
        
        return longest
        