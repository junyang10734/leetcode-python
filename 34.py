# Find First and Last Position of Element in Sorted Array

# Array / Binary Search
# runtime: faster than 13.88%
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find the index of the leftmost appearance of `target`. if it does not
        # appear, return [-1, -1] early.
        l, r = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                l = i
                break
        if l == -1:
            return [-1, -1]

        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        k = len(nums)-1
        while k>=0:
            if nums[k] == target:
                r = k
                break
            k -= 1
        return [l,r]