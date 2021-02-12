# 485. Max Consecutive Ones
# Array

# runtime: faster than 20.78%
# https://blog.csdn.net/fuxuemingzhu/article/details/54561859
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        index = -1
        res = 0
        for i,n in enumerate(nums):
            if n == 0:
                index = i
            else:
                res = max(res, i-index)
        return res