# Elimination Game
# DaC

# https://blog.csdn.net/fuxuemingzhu/article/details/79526571
# runtime: faster than 90.38%
class Solution:
    def lastRemaining(self, n: int) -> int:
        return self.leftToRight(n)
    
    def leftToRight(self, n):
        if n == 1 or n == 2:
            return n
        if n & 1 == 1:
            return 2 * self.rightToLeft((n-1)//2)
        else:
            return 2 * self.rightToLeft(n//2)
        
    def rightToLeft(self, n):
        if n == 1 or n == 2:
            return 1
        if n & 1 == 1:
            return 2 * self.leftToRight((n-1)//2)
        else:
            return 2 * self.leftToRight(n//2) - 1