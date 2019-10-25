# Sum of Two Integers
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# list and sum
# faster than 87.21%
class Solution1(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        l = [a, b]
        return sum(l)


# bit manipulation
# faster than 64.11%
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            temp = a & b
            a = (a ^ b) % 0x100000000
            b = (temp << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000001)