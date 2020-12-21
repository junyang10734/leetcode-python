# 1007. Minimum Domino Rotations For Equal Row

# https://blog.csdn.net/fuxuemingzhu/article/details/88379160
# array / greedy
# running time: faster than 40.98%
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        count = collections.Counter(A+B)
        
        if count.most_common(1)[0][1] < len(A):
            return -1
        target = count.most_common(1)[0][0]
        a_swap, b_swap = 0, 0
        for i in range(len(A)):
            if A[i] == B[i]:
                if A[i] == target:
                    continue
                else:
                    return -1
            elif A[i] == target:
                b_swap += 1
            elif B[i] == target:
                a_swap += 1
            else:
                return -1
        
        return min(a_swap, b_swap)
        