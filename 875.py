# 875. Koko Eating Bananas
# Binary Search

# runtime: faster than 85.45%
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def canFinish(K):
            return sum((p-1)//K + 1 for p in piles) <= H
        
        left, right = 1, max(piles)
        while left <= right:
            mid = (left+right) // 2
            if not canFinish(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left