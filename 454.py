# 4Sum II

# https://blog.csdn.net/fuxuemingzhu/article/details/79473739
# hash / Counter
# running time: faster than 92.36%
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)