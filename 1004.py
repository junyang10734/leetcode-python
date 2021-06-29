# 1004. Max Consecutive Ones III
# Slding Window

# https://leetcode.com/problems/max-consecutive-ones-iii/solution/
# runtime: O(n)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        for j in range(len(nums)):
            k -= 1 - nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return j - i + 1