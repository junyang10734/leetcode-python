# 1792. Maximum Average Pass Ratio
# Heap / Array

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        total_rate = 0
        res = 0
        
        for p,t in classes:
            rate = p/t
            new_rate = (p+1)/(t+1)
            grow = new_rate - rate
            heapq.heappush(heap, (-grow, p, t))
            total_rate += rate
        
        i = 0
        while i < extraStudents:
            grow, p, t = heapq.heappop(heap)
            total_rate -= grow
            p += 1
            t += 1
            rate = p/t
            new_rate = (p+1)/(t+1)
            grow = new_rate - rate
            heapq.heappush(heap, (-grow, p, t))
            i += 1

        return total_rate / len(classes)