# Permutation in String
# Hash / Slide Window
# same as 438

# runtime: faster than 68.29%
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ans = []
        m, n = len(s2), len(s1)
        
        if m < n:
            return False
        
        s1c = Counter(s1)
        s2c = Counter(s2[:n-1])
        
        for i in range(n-1, m):
            s2c[s2[i]] += 1
            if s1c == s2c:
                return True
            
            s2c[s2[i-n+1]] -= 1
            if s2c[s2[i-n+1]] == 0:
                del s2c[s2[i-n+1]]
            
        return False