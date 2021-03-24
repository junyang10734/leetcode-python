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