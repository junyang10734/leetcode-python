# 630. Course Schedule III
# Heap

# https://leetcode.com/problems/course-schedule-iii/discuss/104847/Python-Straightforward-with-Explanation
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        time = 0
        for t,e in sorted(courses, key=lambda x:x[1]):
            time += t
            heapq.heappush(heap, -t)
            while time > e:
                time += heapq.heappop(heap)
        return len(heap)
