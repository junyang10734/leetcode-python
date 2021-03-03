# 1041. Robot Bounded In Circle
# Math
# runtime: faster than 96.39%
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        x, y = 0, 0
        curd = 0
        for i in instructions:
            if i == 'G':
                x += dirs[curd % 4][0]
                y += dirs[curd % 4][1]
            elif i == 'L':
                curd += 1
            elif i == 'R':
                curd -= 1
        return (x == 0 and y == 0) or curd % 4 != 0
