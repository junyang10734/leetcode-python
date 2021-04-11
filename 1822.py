# 1822. Sign of the Product of an Array
# Array

# runtime: O(n)
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for n in nums:
            if n == 0:
                return 0
            p *= n
        return 1 if p > 0 else -1