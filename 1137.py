# 1137. N-th Tribonacci Number
# DP (bottom to top)

# runtime: faster than 80.87%
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        
        n0, n1, n2 = 0, 1, 1
        res = 0
        for i in range(n-2):
            res = n0 + n1 + n2
            n0, n1, n2 = n1, n2, res
        return res