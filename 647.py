# Palindromic Substrings
# String / DP
# Compare with 516

# https://blog.csdn.net/fuxuemingzhu/article/details/79433960

# String
# runtime: faster than 80.74%
class Solution1:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += 1
            
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
                
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        return count


# DP
# runtime: faster than 27.16%
class Solution2:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        start, end, maxL = 0, 0, 0
        dp = [ [0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[i] == s[j]) & ((i-j<2) | dp[j+1][i-1])
                if dp[j][i]:
                    count += 1
            dp[i][i] = 1
            count += 1

        return count
