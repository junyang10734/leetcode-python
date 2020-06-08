# Power of Two
# Math / Bit Manipulation

# https://blog.csdn.net/fuxuemingzhu/article/details/51290981

# Binary
# runtime: faster than 94.71% 
class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count("1") == 1


# Bit operation
# runtime: faster than 31.27% 
class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        return (n & (n-1)) == 0


# runtime: faster than 31.27% 
class Solution3:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<= 0:
            return False
        return (1<<31) % n == 0


# runtime: faster than 94.71%
class Solution4:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 2 == 0:
            n /= 2
        
        return n == 1