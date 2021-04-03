# 295. Find Median from Data Stream
# Design / Heap


# runtime: faster than 84.94%
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap1 = []
        self.heap2 = []
        self.size = 0

    def addNum(self, num: int) -> None:        
        if len(self.heap1) == 0 or num <= -self.heap1[0]:
            if len(self.heap1) <= len(self.heap2):
                heapq.heappush(self.heap1, -num)
            else:
                tmp = heapq.heappop(self.heap1)
                heapq.heappush(self.heap1, -num)
                heapq.heappush(self.heap2, -tmp)
        elif len(self.heap2) == 0 or num > self.heap2[0]:
            if len(self.heap1) >= len(self.heap2):
                heapq.heappush(self.heap2, num)
            else:
                tmp = heapq.heappop(self.heap2)
                heapq.heappush(self.heap1, -tmp)
                heapq.heappush(self.heap2, num)
        else:
            if len(self.heap1) <= len(self.heap2):
                heapq.heappush(self.heap1, -num)
            else:
                heapq.heappush(self.heap2, num)
                
        self.size += 1

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (-self.heap1[0] + self.heap2[0]) / 2
        else:
            return -self.heap1[0] if len(self.heap1) > len(self.heap2) else self.heap2[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()