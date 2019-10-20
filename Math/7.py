# Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31-1 or x < -2**31:
            return 0
        else:
            s = str(x)
            flag = 1  # x>0, flag == 1, else flag == 0
        
            if s[0] == '-':
                flag = 0
                s = s[1:]
        
            ns = '' if flag == 1 else '-'
            i = len(s)-1
            while i>=0:
                ns += s[i]
                i = i - 1
            
            return int(ns) if int(ns) < 2**31-1 and int(ns) > -2**31 else 0
