# Maximum Product Subarray
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/83211451
# runtime: faster than 67.26%

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        l, h = [0] * n, [0] * n
        res = l[0] = h[0] = nums[0]
        
        for i in range(1,n):
            l[i] = min(l[i-1]*nums[i], nums[i], h[i-1]*nums[i])
            h[i] = max(l[i-1]*nums[i], nums[i], h[i-1]*nums[i])
            res = max(res, h[i])
    
        return res


# Less space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        minP = maxP = res = nums[0]
        for i in range(1, len(nums)):
            pre_minP, pre_maxP = minP, maxP
            minP = min(pre_minP * nums[i], pre_maxP * nums[i], nums[i])
            maxP = max(pre_minP * nums[i], pre_maxP * nums[i], nums[i])
            res = max(res, maxP)
        
        return res

