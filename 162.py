# Find Peak Element


# Iterate
# runtime: faster than 77.09%
class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums)-1
        else:
            for i in range(1,len(nums)-1):
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    return i
        return None


# return the index of the maximum
# running time: faster than 77.12%
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))


# Binary Search
# runtime: faster than 92.79%
class Solution3:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid1 = (l+r)//2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                l = mid2
            else:
                r = mid1
        return l
