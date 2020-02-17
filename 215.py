# Kth Largest Element in an Array

# runtime: faster than 97.75% 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]