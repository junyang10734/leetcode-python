# Factorial Trailing Zeroes


# run time: 24 ms, faster than 98.28%
class Solution1:
    def trailingZeroes(self, n: int) -> int:
        num = 0
        while n>=5:
            n = n//5
            num += n
        return num


# run time: 24 ms, faster than 98.28%
class Solution2:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        else:
            return n//5 + self.trailingZeroes(n//5)