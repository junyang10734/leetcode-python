# Number Complement
# Bit Manipulation

# https://blog.csdn.net/fuxuemingzhu/article/details/54562124

# runtime: faster than 96.98%
# map
class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)[2:]
        bin_ans = map(lambda x:'0' if x == '1' else '1', bin_num)
        return int(''.join(bin_ans),2)
