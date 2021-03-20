# 81. Search in Rotated Sorted Array II
# Array

# runtime: faster than 76.12%
class Solution1:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums


# Binary Search
# runtime: faster than 50.13%
class Solution2:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left <= right:
            while left < right and nums[left] == nums[right]:
                left += 1
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False
                