# 509. Fibonacci Number
# Recursive / Iterater / DP


# DP Recursive - Top to Bottom
# runtime: faster than 66.69%
class Solution1:
    def fib(self, n: int) -> int:
        if n < 1:
            return n
        self.cache = [0] * (n+1)
        return self.helper(n)
    
    def helper(self, n):
        if n == 1 or n == 2:
            return 1
        if self.cache[n]:
            return self.cache[n]
        self.cache[n] = self.helper(n-1) + self.helper(n-2)
        return self.cache[n]


# DP Iterater - Bottome to Top
# runtime: faster than 86.41%
class Solution2:
    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        elif n <= 2:
            return 1
        
        dp = [0] * (n+1)
        dp[1] = dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]


# Same as Solution2, but with O(1) space memory
class Solution3:
    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        elif n <= 2:
            return 1
        
        prev = curr = 1

        for i in range(3, n+1):
            s = prev + curr
            prev, curr = curr, s
            
        return curr