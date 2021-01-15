# 342. Power of Four
# Same as 231, 326

# Math

# running time: faster than 63.25% 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n /= 4
        return n == 1
