# Increasing Triplet Subsequence
# runtime: faster than 75.34%
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False