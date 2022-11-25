# 246. Strobogrammatic Number
# String

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {'0': '0', '1':'1', '6':'9', '8':'8', '9':'6'}
        res = ''
        for n in reversed(num):
            if n not in d:
                return False
            res += d[n]
        return res == num