# 1753. Maximum Score From Removing Stones

# Math
# runtime: faster than 33.33%
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:        
        res = 0
        nums = sorted([a, b, c])
        while nums[1]:
            res += 1
            nums[1] -= 1
            nums[2] -= 1
            nums.sort()

        return res