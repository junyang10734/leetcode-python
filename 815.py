# 815. Bus Routes
# BFS

# http://bookshadow.com/weblog/2018/04/10/leetcode-bus-routes/
# runtime: faster than 65.60%
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stopBuses = collections.defaultdict(set)  # 每一站停留的公交车
        busNexts = collections.defaultdict(set)  # 每个公交车可直接换乘的公交车
        for bus, stops in enumerate(routes):
            for stop in stops:
                stopBuses[stop].add(bus)
        for buses in stopBuses.values():
            for bus in buses:
                busNexts[bus] |= set(buses)
                
        
        q = stopBuses[source]
        vset = set(q)
        res = 0
        found = False
        while q and not found:
            new_q = []
            for bus in q:
                if bus in stopBuses[target]:
                    found = True
                    break
                for n in busNexts[bus]:
                    if n not in vset:
                        vset.add(n)
                        new_q.append(n)
            q = new_q
            res += 1
        
        return res if found else -1