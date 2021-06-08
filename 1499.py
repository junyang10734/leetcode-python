# 1499. Max Value of Equation
# Heap

# https://leetcode.com/problems/max-value-of-equation/discuss/709231/JavaPython-Priority-Queue-and-Deque-Solution-O(N)
# runtime: O(nlogn)
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap = []
        res = -inf
        for x,y in points:
            while heap and heap[0][1] < x - k:
                heapq.heappop(heap)
            if heap:
                res = max(res, -heap[0][0] + y + x)
            heapq.heappush(heap, (x-y, x))
            
        return res