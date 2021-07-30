# 600. Non-negative Integers without Consecutive Ones
# DP

# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/discuss/1361379/Python-think-Fibonacci-explained
class Solution:
    def findIntegers(self, n: int) -> int:
        s = bin(n + 1)[2:]
        size = len(s)
        dp = [1, 2] + [0] * (size-2)
        for i in range(2, size):
            dp[i] = dp[i-1] + dp[i-2]
        
        flag, ans = 0, 0
        for i in range(size):
            if s[i] == '0':
                continue
            if flag == 1:
                break
            if i > 0 and s[i-1] == '1':
                flag = 1
            ans += dp[-i-1]
        
        return ans