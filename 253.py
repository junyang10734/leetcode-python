# 253. Meeting Rooms II
# Greedy / Heap / Sort

# runtime: faster than 75.12%
# https://leetcode.com/problems/meeting-rooms-ii/solution/
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])
        
        for i in intervals[1:]:
            if i[0] >= free_rooms[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])
        
        return len(free_rooms)


# labuladong
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        begin, end = [0] * n, [0] * n
        for i in range(n):
            begin[i], end[i] = intervals[i][0], intervals[i][1]
        
        begin.sort()
        end.sort()

        count = 0
        res, i, j = 0, 0, 0
        while i < n and j < n:
            if begin[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
        return res