# Product of Array Except Self
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/79325534
# runtime: faster than 93.00%
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = len(nums)
        res = []
        p = 1
        for i in range(count):
            res.append(p)
            p *= nums[i]
        
        p = 1
        for j in range(count-1,-1,-1):
            res[j] *= p
            p *= nums[j]
        
        return res