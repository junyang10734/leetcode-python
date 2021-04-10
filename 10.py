# 10. Regular Expression Matching
# DP / Recursive

# Recursive
# runtime: faster than 11.47%
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s,p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])
    

# DP
# https://www.youtube.com/watch?v=l3hda49XcDE
# runtime: O(mn)  m = len(s), n = len(p)
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        
        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        
        return dp[-1][-1]
                
