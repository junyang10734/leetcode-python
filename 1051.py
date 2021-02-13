# 1051. Height Checker
# Array

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ordered = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != ordered[i]:
                res += 1
        return res
