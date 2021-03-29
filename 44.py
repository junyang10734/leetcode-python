# 44. Wildcard Matching

# https://leetcode.com/problems/wildcard-matching/solution/

# DP
# runtime: faster than 78.77%
class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        if p == s or (len(set(list(p))) == 1 and p[0] == '*'):
            return True
        if p == '' or s == '':
            return False
        
        dp = [[False]*(s_len+1) for _ in range(p_len+1)]
        dp[0][0] = True
        
        for p_idx in range(1, p_len+1):
            if p[p_idx-1] == '*':
                s_idx = 1
                while not dp[p_idx-1][s_idx-1] and s_idx < s_len + 1:
                    s_idx += 1
                dp[p_idx][s_idx-1] = dp[p_idx-1][s_idx-1]
                while s_idx < s_len+1:
                    dp[p_idx][s_idx] = True
                    s_idx += 1
            elif p[p_idx-1] == '?':
                for s_idx in range(1, s_len+1):
                    dp[p_idx][s_idx] = dp[p_idx-1][s_idx-1]
            else:
                for s_idx in range(1, s_len+1):
                    dp[p_idx][s_idx] = dp[p_idx-1][s_idx-1] and p[p_idx-1] == s[s_idx-1]
        
        return dp[-1][-1]


# BackTrack
# runtime: faster than 94.00%
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0 
        star_idx = s_tmp_idx = -1
        
        while s_idx < s_len:
            if p_idx < p_len and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
                s_idx += 1
                p_idx += 1
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            elif star_idx == -1:
                return False
            else:
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx
        return all(x == '*' for x in p[p_idx:])
