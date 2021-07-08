# 747. Largest Number At Least Twice of Others
# Array

# runtime: O(n)
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1, max2 = -1, -1
        idx = -1
        for i,n in enumerate(nums):
            if n >= max1:
                max1, max2 = n, max1
                idx = i
            elif n > max2:
                max2 = n
        return idx if max1 >= 2 * max2 else -1