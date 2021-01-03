# 1710. Maximum Units on a Truck
# Greedy

# running time: faster than 100.00%
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1])
        boxTypes = boxTypes[::-1]
        res = 0
        i = 0

        while truckSize and i < len(boxTypes):
            if truckSize >= boxTypes[i][0]:
                truckSize -= boxTypes[i][0]
                res += boxTypes[i][0] * boxTypes[i][1]
                i += 1
            else:
                res += truckSize * boxTypes[i][1]
                break

        return res
