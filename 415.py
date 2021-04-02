# 415. Add Strings
# String


# runtime: faster than 96.83%
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1)+int(num2))

# runtime: faster than 57.74%
class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        n1, n2 = len(num1)-1, len(num2)-1     
        carry = 0
        while n1 >= 0 or n2 >= 0:
            x1 = ord(num1[n1]) - ord('0') if n1 >= 0 else 0
            x2 = ord(num2[n2]) - ord('0') if n2 >= 0 else 0
            val = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res = str(val) + res
            n1 -= 1
            n2 -= 1
        
        if carry:
            res = str(carry) + res
        
        return res