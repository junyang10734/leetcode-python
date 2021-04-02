# 1133. Largest Unique Number
# Array / Hash Table

# runtime: faster than 84.03%
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        count = collections.Counter(A)
        A = sorted(list(set(A)), reverse=True)
        for a in A:
            if count[a] == 1:
                return a
        return -1