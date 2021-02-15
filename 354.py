# 354. Russian Doll Envelopes
# DP
# Compare with 300

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0], -x[1]))        
        heights = []
        for e in envelopes:
            heights.append(e[1])
        
        if not heights:
            return 0
        dp = [1 for _ in range(len(heights))]
        for i in range(1, len(heights)):
            for j in range(0, i):
                if heights[j] < heights[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)