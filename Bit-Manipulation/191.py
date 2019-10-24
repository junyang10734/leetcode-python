# Number of 1 Bits
class Solution1(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = 0
        p = 1
        for i in range(32):
            if n & p != 0:
                bits += 1
            p <<= 1
        return bits


class Solution2(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')