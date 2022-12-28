# 1167. Minimum Cost to Connect Sticks
# Greedy / Heap

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        res = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            new_stick = stick1 + stick2
            res += new_stick
            heapq.heappush(sticks, new_stick)
        return res
