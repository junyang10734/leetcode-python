# 70. Climbing Stairs
# DP

# n个台阶有两种到达方式：
# 从 n-1 台阶处 向上1次 1 step
# 从 n-2 台阶处 向上1次 2 

# runtime: O(n)  space: O(n)
class Solution1:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]


# runtime: O(n)  space: O(1)
class Solution2:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1
        res = 1
        for i in range(2, n+1):
            temp = res
            res = first + second
            first = second
            second = res
        
        return res