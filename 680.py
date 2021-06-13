# 680. Valid Palindrome II
# String

# https://leetcode.com/problems/valid-palindrome-ii/discuss/107718/Easy-to-Understand-Python-Solution
# runtime: O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        count = 0
        while i < j:
            if s[i] != s[j]:
                one, two = s[i:j], s[i+1: j+1]
                return one == one[::-1] or two == two[::-1]
            i += 1
            j -= 1
        return True
