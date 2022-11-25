# 1099. Two Sum Less Than K
# two pointers

# time: O(n)
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return -1
        
        nums.sort()
        res = -1
        i, j = 0, len(nums)-1
        while i < j:
            s = nums[i] + nums[j]
            if s < k:
                res = max(s, res)
                i += 1
            else:
                j -= 1
        
        return res