# Hamming Distance
# Bit Manipulation

# String
# runtime: faster than 91.20% 
class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        a = str(bin(x))[2:]
        b = str(bin(y))[2:]
        dis = 0
        len1, len2 = len(a), len(b)
        _len = 0
        
        if len1 > len2:
            c = len1 - len2
            b = '0'*c + b
            _len = len1
        elif len1 < len2:
            c = len2 - len1
            a = '0'*c + a
            _len = len2
        else:
            _len = len1
        

        for i in range(_len):
            if a[i] != b[i]:
                dis += 1
        
        return dis


# https://blog.csdn.net/fuxuemingzhu/article/details/54138423

# XOR + count
# runtime: faster than 98.34%
class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


# XOR + cycle iteration
# runtime: faster than 91.20% 
class Solution3:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x or y:
            if (x & 1) ^ (y & 1):
                res += 1
            x >>= 1
            y >>= 1
                
        return res


# XOR + one iteration
# runtime: faster than 74.22%
class Solution4:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        res = 0
        while xor:
            res += xor & 1
            xor >>= 1
        
        return res
