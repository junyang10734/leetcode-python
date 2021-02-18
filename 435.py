# 435. Non-overlapping Intervals
# Greedy
# Compare with 452

# runtime: faster than 94.10%
# 注意，需要算出最多的非重合区间，然后用总长度减去即可
# 直接计算最多的减区间数量是错误的，达不到贪心的效果
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        sortedIntervals = sorted(intervals, key=(lambda x:x[1]))
        count = 1
        end = sortedIntervals[0][1]
        for interval in sortedIntervals:
            start = interval[0]
            if start >= end:
                count += 1
                end = interval[1]
        
        return len(intervals) - count