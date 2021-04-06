# 158. Read N Characters Given Read4 II - Call multiple times
# String

# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/discuss/193873/Most-elegant-and-simple-solution-in-Python
# runtime: faster than 58.54%

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
class Solution:
    def __init__(self):
        self.q = []
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n:
            if self.q:
                buf[i] = self.q.pop(0)
                i += 1
            else:
                buf4 = ['']*4
                v = read4(buf4)
                if v == 0:
                    break
                self.q += buf4[:v]
        return i