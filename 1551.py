# 1551. Minimum Operations to Make Array Equal
# Math

# runtime: faster than 49%
class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        for i in range(1, n, 2):
            res += n - i
        return res