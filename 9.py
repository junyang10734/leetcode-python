# 9. Palindrome Number
# easy

# runtime: faster than 64.71%
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x != 0):
            return False
        
        res = 0
        init = x
        while x > 0:
            res = res*10 + x%10
            x //= 10

        return res == init or res == init/10