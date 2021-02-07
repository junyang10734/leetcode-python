# 1752. Check if Array Is Sorted and Rotated
# Array

class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        if N <= 2:
            return True
        
        idx = 0
        for i in range(1,N):
            if nums[i] < nums[i-1]:
                idx = i
                break
            if i == N-1:
                return True
            
        for i in range(idx+1, N):
            if nums[i] < nums[i-1]:
                return False
        
        return nums[0] >= nums[-1]