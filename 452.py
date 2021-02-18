# 452. Minimum Number of Arrows to Burst Balloons
# Greedy
# Compare with 435

# runtime: faster than 44.15%
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        
        sortedPoints = sorted(points, key=lambda x:x[1])
        count = 1
        end = sortedPoints[0][1]
        
        for point in sortedPoints:
            start = point[0]
            if start > end:
                count += 1
                end = point[1]
        return count