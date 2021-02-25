# 1048. Longest String Chain
# compare: 300, 673
# Hash Table / DP

# https://xingxingpark.com/Leetcode-1048-Longest-String-Chain/
# running time: faster than 62.16%
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i+1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())
