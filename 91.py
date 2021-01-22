# 91. Decode Ways
# DP

# https://leetcode.com/problems/decode-ways/discuss/163707/Python-From-O%28N%29-Space-To-O%281%29-Space-Solutions

# runtime: faster than 97.37%
class Solution1:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[0] = 1
        
        for i in range(1, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':
                dp[i] += dp[i-2]
        
        return dp[-1]
            

# runtime: faster than 70.42%
# less space
class Solution2:
    def numDecodings(self, s: str) -> int:
        a, b, c = 0, 1, 0
        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                c = b
            if i != 1 and '09' < s[i-2:i] < '27':
                c += a
            a, b, c = b, c, 0
        
        return b           