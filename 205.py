# Isomorphic Strings
# Hast Table

# runtime: faster than 69.47%
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}
        
        for i,a in enumerate(s):
            if a in d1 and d1[a] != t[i]:
                return False
            if t[i] in d2 and a != d2[t[i]]:
                return False
            d1[a] = t[i]
            d2[t[i]] = a
        return True