# Search in Rotated Sorted Array


# Binary Search
# runtime: faster than 86.30%
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            mid = int((left+right)/2)
            if target == nums[mid]:
                return mid
            elif nums[left] <= nums[mid]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1