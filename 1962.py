# 1962. Remove Stones to Minimize the Total
# heap

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        removes = 0
        piles = [-x for x in piles]
        heapq.heapify(piles)
        for i in range(k):
            num = -heapq.heappop(piles)
            remove = num // 2
            removes += remove
            heapq.heappush(piles, -(num - remove))
        
        return total - removes