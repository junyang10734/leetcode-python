# 50. Pow(x, n)

# https://blog.csdn.net/fuxuemingzhu/article/details/82960833

# recursive
# run time: faster than 94.27%
class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        if n % 2:
            return x*self.myPow(x,n-1)
        else:
            return self.myPow(x*x,n/2)


# run time: faster than 83.91%  
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        
        ans = 1
        while n:
            if n % 2:
                ans *= x
            n >>= 1
            x *= x
            
        return ans