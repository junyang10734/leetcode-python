# 1229. Meeting Scheduler
# Two Pointers

# https://leetcode.com/problems/meeting-scheduler/solution/
# runtime: O(MlogM+NlogN)
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        p1 = p2 = 0
        
        while p1 < len(slots1) and p2 < len(slots2):
            intersect_right = min(slots1[p1][1], slots2[p2][1])
            intersect_left = max(slots1[p1][0], slots2[p2][0])
            if intersect_right - intersect_left >= duration:
                return [intersect_left, intersect_left + duration]
            if slots1[p1][1] < slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return []