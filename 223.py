# Rectangle Area
# Math

# https://blog.csdn.net/fuxuemingzhu/article/details/82973125
# runtime: faster than 27.12%
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = (D - B) * (C - A)
        area2 = (H - F) * (G - E)
        x = min(C, G) - max(A, E)
        y = min(D, H) - max(B, F)
        area3 = 0
        if x > 0 and y > 0:
            area3 = x * y
        
        return area1 + area2 - area3
