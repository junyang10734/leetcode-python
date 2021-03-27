# 870. Advantage Shuffle
# Array / Greedy

# https://blog.csdn.net/fuxuemingzhu/article/details/82796298
# runtime: faster than 75.64% 
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A = collections.deque(sorted(A))
        B = collections.deque(sorted((b,i) for i,b in enumerate(B)))
        res = [-1]*len(A)
        for i in range(len(A)):
            a = A.popleft()
            b = B[0]
            if a > b[0]:
                B.popleft()
            else:
                b = B.pop()
            res[b[1]] = a
        return res