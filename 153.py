# Find Minimum in Rotated Sorted Array
# Array

# Binary Search
# runtime: faster than 90.69% 
class Solution1:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums)-1
        
        if nums[0] < nums[right]:
            return nums[0]
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

# runtime: faster than 71.63%
class Solution1:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


# DaC
# https://zxi.mytechroad.com/blog/leetcode/leetcode-153-find-minimum-in-rotated-sorted-array/
# faster than 54.30%
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        def dac(nums, l, r):
            if l + 1 >= r:
                return min(nums[l], nums[r])
            if nums[l] < nums[r]:
                return nums[l]
            
            mid = l + (r - l) // 2
            return min(dac(nums, l, mid), dac(nums, mid+1, r))
        
        return dac(nums, 0, len(nums)-1)


# runtime: faster than 71.63%
class Solution3:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)