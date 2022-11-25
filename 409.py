# 409. Longest Palindrome
# Hash Table / Greedy

# time: O(n)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = collections.defaultdict(int)
        for i in s:
            d[i] += 1
        
        maxv = 0
        res = 0
        for k,v in d.items():
            if v % 2 == 0:
                res += v
            else:
                maxv = max(maxv, v)
                res += (v - 1) 
            
        return res + 1 if maxv else res
