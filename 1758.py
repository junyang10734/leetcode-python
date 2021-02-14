# 1758. Minimum Changes To Make Alternating Binary String
# String

class Solution:
    def minOperations(self, s: str) -> int:
        res = sum(i % 2 == int(c) for i,c in enumerate(s))
        return min(res, len(s)-res)
