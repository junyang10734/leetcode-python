# Power of Three
# Same as 231, 342

# loop
# faster than 30.01%
class Solution1(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 1:
            if n%3 == 0:
                n /= 3
            else:
                return False
        return True


# math
# faster than 73.10%
class Solution2(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        return (math.log10(n) / math.log10(3)) % 1 == 0