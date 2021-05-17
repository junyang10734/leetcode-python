# 161. One Edit Distance
# String

# runtime: O(n)
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        if len(s) == len(t):
            count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    if count == 1:
                        return False
                    count += 1
        else:
            if len(s) > len(t):
                s, t = t, s
            
            if len(t) - len(s) > 1:
                return False
            i, j = 0, 0
            count = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    if count > 0:
                        return False
                    count += 1
                    j += 1
        return True