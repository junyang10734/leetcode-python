# 1564. Put Boxes Into the Warehouse I
# Greedy

# https://leetcode.com/problems/put-boxes-into-the-warehouse-i/solution/
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i-1], warehouse[i])
        
        boxes.sort()
        count = 0
        for room in reversed(warehouse):
            if count < len(boxes) and boxes[count] <= room:
                count += 1
        return count