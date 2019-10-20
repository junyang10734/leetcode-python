# Excel Sheet Column Number
# ord(x) -- compute the ascii code, ord(A) = 65
class Solution:
    def titleToNumber(self, s: str) -> int:
        sum = 0
        l = len(s)
        for i,item in enumerate(s):
            sum += (ord(item)-64)*(26**(l-i-1))

        return sum
                                   