# 459. Repeated Substring Pattern

# runtime: faster than 98.36% 
class Solution1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i = (s+s)[1:-1].find(s)
        if i == -1:
            return False
        else:
            return True

# runtime: faster than 72.83%
class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        for i in range(1, N//2+1):
            if N % i == 0:
                if s[:i]*(N//i) == s:
                    return True
        return False