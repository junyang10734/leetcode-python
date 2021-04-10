# 401. Binary Watch
# Bit Manipulation

# https://leetcode.com/problems/binary-watch/discuss/88458/Simple-Python%2BJava
# runtime: faster than 88.85%
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return ['%d:%02d' % (h, m) for h in range(12) for m in range(60) if (bin(h) + bin(m)).count('1') == turnedOn]