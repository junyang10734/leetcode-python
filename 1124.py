# 1124. Longest Well-Performing Interval

# https://leetcode.com/problems/longest-well-performing-interval/discuss/334565/JavaC%2B%2BPython-O(N)-Solution-Life-needs-996-and-669
# runtime: faster than 43.75%
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = score = 0
        seen = {}
        for i,h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res