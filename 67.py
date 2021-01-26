# 67. Add Binary

# https://medium.com/@edward.zhou/leetcode-67-add-binary-998ea7ee490e
# runtime: faster than 23.79%
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        carry = 0
        res = ''
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            carry, remain = divmod(carry, 2)
            res += str(remain)
        
        return res[::-1]
