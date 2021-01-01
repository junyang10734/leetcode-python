# 801. Minimum Swaps To Make Sequences Increasing

# DP
# https://blog.csdn.net/fuxuemingzhu/article/details/83269027
# running time: faster than 36.47%
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        keep, swap = 0, 1
        for i in range(1, len(A)):
            curkeep, curswap = float('inf'), float('inf')
            if A[i] > A[i-1] and B[i] > B[i-1]:
                curkeep = keep
                curswap = swap + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                curkeep = min(curkeep, swap)
                curswap = min(keep + 1, curswap)
                
            keep, swap = curkeep, curswap
        
        return min(keep, swap)