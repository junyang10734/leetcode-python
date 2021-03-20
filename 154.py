# Find Minimum in Rotated Sorted Array II
# Array

# Dac
# https://zxi.mytechroad.com/blog/divide-and-conquer/leetcode-154-find-minimum-in-rotated-sorted-array-ii/
# faster than 98.91% 
class Solution1:
    def findMin(self, nums: List[int]) -> int:
        def dac(nums, l, r):
            if r - l <= 1:
                return min(nums[l], nums[r])
            if nums[l] < nums[r]:
                return nums[l]
            
            mid = l + (r - l) // 2
            return min(dac(nums, l, mid), dac(nums, mid+1, r))
        
        return dac(nums, 0, len(nums)-1)


# Binary Search
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/48908/Clean-python-solution
# faster than 71.63%
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[right] == nums[mid]:
                right -= 1
            else:
                right = mid
        return nums[left]


# runtime: faster than 71.63%
class Solution3:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)