# 1288. Remove Covered Intervals
# Array / Sorting

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1]))
        left, right = intervals[0][0], intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            intv = intervals[i]
            if intv[0] >= left and intv[1] <= right:
                res += 1
            elif intv[0] >= left and intv[1] >= right:
                right = intv[1]
            elif intv[1] > right:
                left, right = intv[0], intv[1]

        return len(intervals) - res