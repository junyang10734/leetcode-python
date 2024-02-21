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
    

# https://labuladong.github.io/algo/di-san-zha-24031/shu-xue-yu-659f1/chang-yong-13a76/#%E4%BA%8C%E3%80%81n-n-1-%E7%9A%84%E8%BF%90%E7%94%A8
class Solution3:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n != 0:
            n = n & (n-1)
            bits += 1
        return bits