# 713. Subarray Product Less Than K

# Two pointers (sliding window)

# https://blog.csdn.net/fuxuemingzhu/article/details/83047699
# running time: faster than 63.76%
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        prod = 1
        l, r = 0, 0
        res = 0
        
        while r < N:
            prod *= nums[r]
            while l <= r and prod >= k:
                prod /= nums[l]
                l += 1
            res += r - l + 1
            r += 1
            
        return res
