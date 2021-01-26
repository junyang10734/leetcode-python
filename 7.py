# Reverse Integer


# https://blog.csdn.net/fuxuemingzhu/article/details/79258815
# cmp: (a > b) - (a < b) 比较ab大小
class Solution1:
    def reverse(self, x: int) -> int:
        n = ((x > 0) - (x < 0)) * int(str(abs(x))[::-1])
        return n if n.bit_length() < 32 else 0


class Solution2:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        
        r = flag * int(str(x)[::-1])
        
        return r if -2**31 <= r <= 2**31 - 1 else 0 


class Solution3:
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
