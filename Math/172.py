# Factorial Trailing Zeroes
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        
        while n>= 5:
            a = n//5
            num += a
            n = a
        
        return num
