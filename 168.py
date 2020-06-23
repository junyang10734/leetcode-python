# Excel Sheet Column Title
# Math

# https://blog.csdn.net/NXHYD/article/details/71712117
# runtime: faster than 72.65%
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n >= 1:
            n -= 1
            res = chr(int(n % 26 + ord('A'))) + res
            n /= 26
        return res