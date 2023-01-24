# 926. Flip String to Monotone Increasing
# Array / DP

# https://blog.csdn.net/fuxuemingzhu/article/details/83247054

# prefix
# running time: faster than 35.82%
class Solution1:
    def minFlipsMonoIncr(self, S: str) -> int:
        p = [0]
        for s in S:
            p.append(p[-1] + int(s))
        
        return min(p[j] + len(S)-j-(p[-1]-p[j]) for j in range(len(p)))


# DP
# running time: faster than 74.25%
class Solution2:
    def minFlipsMonoIncr(self, S: str) -> int:
        one, zero = 0, 0
        
        for s in S:
            if s == '0':
                one = min(one, zero) + 1
            else:
                one = min(one, zero)
                zero += 1
        
        return min(one, zero)


# DP
# https://leetcode.com/problems/flip-string-to-monotone-increasing/solutions/2912351/flip-string-to-monotone-increasing/
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        num = 0
        for i in range(1, len(s)+1):
            if s[i-1] == '1':
                dp[i] = dp[i-1]
                num += 1
            else:
                dp[i] = min(num, dp[i-1]+1)
        return dp[-1]