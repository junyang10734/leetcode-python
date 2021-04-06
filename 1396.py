# 1396. Design Underground System
# Design / Hash Table

# https://leetcode.com/problems/design-underground-system/solution/
# runtime: faster than 65.24%
class UndergroundSystem:

    def __init__(self):
        self.checkin_data = {}
        self.journey_data = collections.defaultdict(lambda: [0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_data[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkin_data.pop(id)
        self.journey_data[(startStation, stationName)][0] += (t - startTime)
        self.journey_data[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, count = self.journey_data[(startStation, endStation)]
        return time / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)