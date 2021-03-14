# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
# Array

# runtime: faster than 98.58%
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        
        diffH = [horizontalCuts[i+1] - horizontalCuts[i] for i in range(len(horizontalCuts)-1)]
        diffW = [verticalCuts[i+1] - verticalCuts[i] for i in range(len(verticalCuts)-1)]
        maxH, maxW = max(diffH), max(diffW)
        return (maxH*maxW) % (10**9+7)