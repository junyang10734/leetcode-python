# 215. Kth Largest Element in an Array

# Sort
# runtime: faster than 97.75% 
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


# heapq 大根堆
# runtime: faster than 99.13% 
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


# QuickSort
# runtime: O(n)
class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums)-1
        k = len(nums) - k

        while left <= right:
            index = self.partition(nums, left, right)
            if index == k:
                return nums[index]
            elif index < k:
                left = index + 1
            else:
                right = index - 1

        return -1
    
    def partition(self, nums, left, right):
        pivot = nums[left]
        i, j = left + 1, right

        while i <= j:
            while i < right and nums[i] <= pivot:
                i += 1
            while j > left and nums[j] >= pivot:
                j -= 1
            
            if i >= j:
                break
            
            nums[i], nums[j] = nums[j], nums[i]
        
        nums[left], nums[j] = nums[j], nums[left]
        return j