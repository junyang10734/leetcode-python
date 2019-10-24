# Happy Number

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = {}
        
        while True:
            d[n] = True
            sum = 0
            while n>0:
                sum += (n%10)**2
                n /= 10
            if sum == 1:
                return True
            elif sum in d:
                return False
            else:
                n = sum