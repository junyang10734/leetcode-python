# Find First and Last Position of Element in Sorted Array

# Array / Binary Search
# runtime: faster than 13.88%
class Solution1:
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


# https://blog.csdn.net/fuxuemingzhu/article/details/83273084
# running time: faster than 68.61%
class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:
            return [-1,-1]
        return [left, right-1]


# write bisect.bisect_left and bisect.bisect_right by self
# running time: faster than 68.61%
class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.lower_bound(nums, target)
        right = self.upper_bound(nums, target)
        if left == right:
            return [-1,-1]
        return [left, right - 1]
        
        
    def lower_bound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
        

    def upper_bound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l