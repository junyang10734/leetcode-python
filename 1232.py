# Check If It Is a Straight Line
# Array / Math

# runtime: fasther than 92.34%
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        length = len(coordinates)
        if length <= 1:
            return False
        elif length == 2:
            return True
        else:
            p0, p1 = coordinates[0], coordinates[1]
            x0, y0 = p0[0], p0[1]
            x1, y1 = p1[0], p1[1]
            if x1 == x0:
                for i in range(2,len(coordinates)):
                    pi = coordinates[i]
                    xi = pi[0]
                    if xi != x0:
                        return False
            else:     
                k = (y1 - y0) / (x1 - x0)
                for i in range(2,len(coordinates)):
                    pi = coordinates[i]
                    xi, yi = pi[0], pi[1]
                    if xi == x0:
                        return False
                    ki = (yi - y0) / (xi - x0)
                    if ki != k:
                        return False
            
            return True