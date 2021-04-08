# 504. Base 7
# Math

# runtime: faster than 55%
class Solution1:
    def convertToBase7(self, num: int) -> str:
        flag = False
        if num < 0:
            num = -num
            flag = True
        res = 0
        i = 0
        while num > 0:
            tmp = (num % (7 ** (i+1))) // (7 ** i)
            res = tmp * (10**i) + res
            num -= tmp * (7 ** i)
            i += 1
        return str(-res) if flag else str(res)


# https://leetcode.com/problems/base-7/discuss/98364/JavaC%2B%2BPython-Iteration-and-Recursion
# runtime: faster than 55%
class Solution2:
    def convertToBase7(self, num: int) -> str:
        n, res = abs(num), ''
        while n:
            res = str(n % 7) + res
            n //= 7
        return '-' * (num < 0) + res or "0"