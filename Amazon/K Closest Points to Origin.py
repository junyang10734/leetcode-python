# leetcode 973. K Closest Points to Origin
class Solution2:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda p:p[0]**2 + p[1]**2)
        return points[:K]