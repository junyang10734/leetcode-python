# Subarray Sum Equals K
# Array / Hash Table

# https://blog.csdn.net/fuxuemingzhu/article/details/82767119
# runtime: faster than 75.99%
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        d[0] = 1
        s = res = 0
        
        for i in range(len(nums)):
            s += nums[i]
            if s-k in d:
                res += d[s-k]   
            d[s] += 1
            
        return res