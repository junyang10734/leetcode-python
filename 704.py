# 704. Binary Search
# Array / Binary Search

# runtime: faster than 68.51%
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1