# 1736. Latest Time by Replacing Hidden Digits
# String

class Solution:
    def maximumTime(self, time: str) -> str:
        res = ''
        for i,t in enumerate(time):
            if t == '?':
                if i == 0:
                    res += '2'
                elif i == 1:
                    res += '3' if res[0] == '2' else '9'
                elif i == 3:
                    res += '5'
                elif i == 4:
                    res += '9'
            else:
                res += t
        
        if res[0] == '2' and res[1] > '3':
            res = '1' + res[1:]
        
        return res
                    