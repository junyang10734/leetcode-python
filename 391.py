# 391. Perfect Rectangle
# Array

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        x1, y1 = float("inf"), float("inf")
        x2, y2 = -float("inf"), -float("inf")
        points = set()
        actual_area = 0

        for m1, n1, m2, n2 in rectangles:
            # 计算完美矩形的理论顶点坐标
            x1, y1 = min(x1, m1), min(y1, n1)
            x2, y2 = max(x2, m2), max(y2, n2)
            # 累加小矩形的面积
            actual_area += (m2 - m1) * (n2 - n1)
            # 记录最终形成的图形中的顶点
            p1, p2, p3, p4 = (m1, n1), (m1, n2), (m2, n1), (m2, n2)
            for p in [p1, p2, p3, p4]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)

        # 判断面积是否相同
        expected_area = (x2 - x1) * (y2 - y1)
        if expected_area != actual_area:
            return False

        # 判断最终留下的顶点个数是否为 4
        if len(points) != 4:
            return False

        # 判断留下的 4 个顶点是否是完美矩形的顶点
        if (x1, y1) not in points:
            return False
        if (x1, y2) not in points:
            return False
        if (x2, y1) not in points:
            return False
        if (x2, y2) not in points:
            return False

        return True
