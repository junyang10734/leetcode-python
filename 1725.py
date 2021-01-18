# 1725. Number Of Rectangles That Can Form The Largest Square

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res = [min(i) for i in rectangles]
        return Counter(res)[max(res)]