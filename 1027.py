# 1027. Longest Arithmetic Subsequence

# https://xingxingpark.com/Leetcode-1027-Longest-Arithmetic-Sequence/
# runtime: faster than 50.01%
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                dp[(j, A[j] - A[i])] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())
