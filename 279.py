# Perfect Squares
# Math / DP

# https://blog.csdn.net/fuxuemingzhu/article/details/51284292
# math
# runtime: faster than 92.18% 
class Solution1:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n /= 4
        
        if n % 8 == 7:
            return 4
        
        a = 0
        while a*a < n:
            b = 0
            while b*b <= n - a*a:
                if a*a + b*b == n:
                    a = 1 if a > 0 else 0
                    b = 1 if b > 0 else 0
                    return a + b
                b += 1
            a += 1
        
        return 3


# DP
# runtime: faster than 8.72%
class Solution2:
    def numSquares(self, n: int) -> int:
        dp = [sys.maxsize] * (n+1)

        m = 0
        while m*m <= n:
            dp[m*m] = 1
            m += 1
        
        i = 0
        while i <= n:
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
                j += 1
            i += 1
        
        return dp[n]   


# DP
# clearer than solution2
# runtime: faster than 26.14%
class Solution3:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0], dp[1] = 0, 1

        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1

        return dp[n]