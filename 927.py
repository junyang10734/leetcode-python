# 927. Three Equal Parts
# Math

# https://leetcode.com/problems/three-equal-parts/solution/
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        IMP = [-1, -1]
        s = sum(arr)
        if s % 3:
            return IMP
        t = s / 3
        if t == 0:
            return [0, len(arr)-1]
        
        breaks = []
        tmp = 0
        for i,n in enumerate(arr):
            if n:
                tmp += n
                if tmp in {1, t+1, 2*t+1}:
                    breaks.append(i)
                if tmp in {t, 2*t, 3*t}:
                    breaks.append(i)
        i1, j1, i2, j2, i3, j3 = breaks
        
        if not (arr[i1: j1+1] == arr[i2: j2+1] == arr[i3: j3+1])    :
            return IMP
        x = i2 - j1 - 1
        y = i3 - j2 - 1
        z = len(arr) - j3 - 1
        if x < z or y < z:
            return IMP
        j1 += z
        j2 += z
        return [j1, j2+1]
                