# Next Permutation
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/82113409
# runtime: faster than 51.21% 
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        
        self.reverse(nums, i, n-1)
        if i > 0:
            for j in range(i, n):
                if nums[j] > nums[i-1]:
                    self.swap(nums, i-1, j)
                    break
    
    def reverse(self, nums, i, j):
        for k in range(i, (i+j)//2 + 1):
            self.swap(nums, k, i+j-k)
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]