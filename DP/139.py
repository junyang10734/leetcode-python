# 139 Word Break

# Runtime: faster than 51.45%
# https://blog.csdn.net/fuxuemingzhu/article/details/79368360
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        
        return dp.pop()