# Bitwise AND of Numbers Range
# Bit Manipulation

# https://blog.csdn.net/fuxuemingzhu/article/details/79495633
# runtime: faster than 68.52%
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        
        return m << i