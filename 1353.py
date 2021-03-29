# 1353. Maximum Number of Events That Can Be Attended
# Greedy / Sort / Heap

# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510263/JavaC%2B%2BPython-Priority-Queue
# runtime: faster than 90.00%
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        heap = []
        res = day = 0
        
        while events or heap:
            if not heap:
                day = events[-1][0]
            while events and events[-1][0] <= day:
                heapq.heappush(heap, events.pop()[1])
            heapq.heappop(heap)
            res += 1
            day += 1
            while heap and heap[0]<day:
                heapq.heappop(heap)
        return res