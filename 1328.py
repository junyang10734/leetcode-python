# 1328. Break a Palindrome
# String

# runtime: faster than 98.85%
class Solution1:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        
        v = ''
        for i in range(len(palindrome)):
            if palindrome[i] != 'a':
                v = palindrome[:i] + 'a' + palindrome[i+1:]
            if v == v[::-1]:
                continue
            return v
        
        if palindrome[-1] == 'a':
            return palindrome[:-1] + 'b'
        
        return palindrome[:-1] + 'a'



# runtime: faster than 80.04%
class Solution2:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ''
        for i in range(n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        return palindrome[:-1] + 'b'