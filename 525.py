# Contiguous Array
# Hash Table

https://blog.csdn.net/fuxuemingzhu/article/details/82667054
# runtime: faster than 62.20%
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        idx_map = {}
        idx_map[0] = -1
        total_sum = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                total_sum -= 1
            else:
                total_sum += 1
            
            if total_sum in idx_map:
                ans = max(ans, i-idx_map[total_sum])
            else:
                idx_map[total_sum] = i

        return ans