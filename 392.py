# Is Subsequence
# String

# runtime: faster than 97.95% 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        
        for i in t:
            if i == s[0]:
                s = s[1:]

                if s == '':
                    return True
        
        return s == ''