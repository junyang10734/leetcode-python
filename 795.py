# 795. Number of Subarrays with Bounded Maximum
# Array

# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/117723/Python-standard-DP-solution-with-explanation
# runtime: O(n)
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = 0
        dp = 0
        prev = -1
        for i,num in enumerate(nums):
            if num < left and i > 0:
                res += dp
            elif num > right:
                dp = 0
                prev = i
            elif left <= num <= right:
                dp = i - prev
                res += dp
        return res