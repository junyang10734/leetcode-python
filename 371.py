# Sum of Two Integers
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# list and sum
# faster than 91.12%
class Solution1(object):
    def getSum(self, a: int, b: int) -> int:
        l = [a, b]
        return sum(l)


# bit manipulation
# https://blog.csdn.net/fuxuemingzhu/article/details/79379939
# faster than 97.13%
class Solution2:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
