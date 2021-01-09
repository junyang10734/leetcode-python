# 769. Max Chunks To Make Sorted
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/80482014
# running time: faster than 54.96% 
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res, premax = 0, 0
        for i,n in enumerate(arr):
            premax = max(n, premax)
            if premax == i:
                res += 1
        return res