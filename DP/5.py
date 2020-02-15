# Longest Palindromic Substring
# runtime: faster than 73.24%
# https://www.youtube.com/watch?v=nSFWpXuNfyw
class Solution1:
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


# dp
# runtime: faster than 36.26%
# https://blog.csdn.net/fuxuemingzhu/article/details/79573621
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        
        dp = [[0] * n for _ in range(n)]
        start, end, maxL = 0, 0, 0
        for i in range(n):
            for j in range(i):
                if s[j] == s[i] and (j==i-1 or dp[j+1][i-1]==1):
                    dp[j][i] = 1
                if dp[j][i] == 1 and maxL < i-j+1:
                    maxL = i-j+1
                    start = j
                    end = i
            dp[i][i] = 1
        return s[start:end+1]