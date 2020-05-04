# Minimum Time Visiting All Points
# Array

# runtime: faster than 64.31%
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        step = 0
        for i in range(len(points)-1):
            x = abs(points[i+1][0] - points[i][0])
            y = abs(points[i+1][1] - points[i][1])
            if x == 0:
                step += y
            elif y == 0:
                step += x
            else:
                n = x - y
                if n>0:
                    step += y
                    step += n
                else:
                    step += x
                    step -= n
        return step