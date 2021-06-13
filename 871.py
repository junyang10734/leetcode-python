# 871. Minimum Number of Refueling Stops
# DP / Heap

# https://leetcode.com/problems/minimum-number-of-refueling-stops/solution/

# DP
# runtime: O(n**2)
class Solution1:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)
        for i,d in enumerate(dp):
            if d >= target:
                return i
        return -1


# Heap
# runtime: O(n*logn)
class Solution2:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        stations.append((target, inf))
        res = prev = 0
        
        for location, capacity in stations:
            startFuel -= location - prev
            while heap and startFuel < 0:
                startFuel += -heapq.heappop(heap)
                res += 1
            if startFuel < 0:
                return -1
            heapq.heappush(heap, -capacity)
            prev = location
        return res