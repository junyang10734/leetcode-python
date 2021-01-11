# 374. Guess Number Higher or Lower
# Binary Search

# running time: faster than 5.05%
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i, j = 1, n
        mid = i
        while i <= j:
            mid = (i+j)//2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                j = mid - 1
            else:
                i = mid + 1
        
        return mid