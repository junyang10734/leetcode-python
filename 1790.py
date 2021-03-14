# 1790. Check if One String Swap Can Make Strings Equal
# String

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        n = len(s1)
        arr = []
        for i in range(n):
            if s1[i] != s2[i]:
                arr.append(i)
        
        if len(arr) == 2:
            return s1[arr[0]] == s2[arr[1]] and s1[arr[1]] == s2[arr[0]]
        else:
            return False