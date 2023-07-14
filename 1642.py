# 1642. Furthest Building You Can Reach
# Heap

# https://leetcode.com/problems/furthest-building-you-can-reach/solution/

# Heap
# runtime: O(nlogn)
# 全部用ladder，当没有ladder时，找到ladder攀登的最小高度，用brick代替
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = []
        for i in range(len(heights)-1):
            climb = heights[i+1] - heights[i]
            if climb <= 0:
                continue
            heapq.heappush(ladder_allocations, climb)
            if len(ladder_allocations) <= ladders:
                continue
            bricks -= heapq.heappop(ladder_allocations)
            if bricks < 0:
                return i
        return len(heights)-1


# Heap
# 全部用brick，知道没有brick可用，找到最大高度差用ladder代替
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        usedBricks = []
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            
            heapq.heappush(usedBricks, -diff)
            bricks -= diff
            if bricks < 0 and ladders <= 0:
                return i
            if bricks < 0:
                ladders -= 1
                bricks -= heapq.heappop(usedBricks)

        return len(heights) - 1