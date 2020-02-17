# Longest Palindromic Substring
# runtime: faster than 73.24%
# https://www.youtube.com/watch?v=nSFWpXuNfyw
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            p1 = self.getp(s,i,i)
            p2 = self.getp(s,i,i+1)
            p = p1 if len(p1) > len(p2) else p2
            ans = p if len(p) > len(ans) else ans
        return ans
            
    
    def getp(self, s:str, l:int, r:int) -> str:
        while l>=0 and r<len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]