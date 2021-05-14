# 906. Super Palindromes
# Math

# https://leetcode.com/problems/super-palindromes/solution/
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L, R = int(left), int(right)
        MAGIC = 100000
        
        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x //= 10
            return ans
        
        def is_palindrome(x):
            return x == reverse(x)
        
        res = 0
        for k in range(MAGIC):
            s = str(k)
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(v):
                res += 1
                
        for k in range(MAGIC):
            s = str(k)
            t = s + s[::-1]
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(v):
                res += 1
        return res