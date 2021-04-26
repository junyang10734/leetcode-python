# 703. Kth Largest Element in a Stream
# Heap / Design

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) >= self.k:
            if val <= self.heap[0]:
                return self.heap[0]
            else:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
                return self.heap[0]
        else:
            heapq.heappush(self.heap, val)
            return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)