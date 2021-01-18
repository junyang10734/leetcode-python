# 836. Rectangle Overlap
# Math

# https://leetcode.com/problems/rectangle-overlap/solution/

# Check Position
# running time: faster than 55.90%
class Solution1:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False

        if rec1[2] <= rec2[0] or rec1[3] <= rec2[1] or rec2[2] <= rec1[0] or rec2[3] <= rec1[1]:
            return False
        
        return True


# Check Area
# running time: faster than 95.45%
class Solution2:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        p_x1, p_y1, p_x2, p_y2 = rec1
        q_x1, q_y1, q_x2, q_y2 = rec2
        return (min(p_x2, q_x2) > max(p_x1, q_x1)) and (min(p_y2, q_y2) > max(p_y1, q_y1))