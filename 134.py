# Gas Station
# Array

# runtime: faster than 94.43%
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank, need, start = 0, 0, 0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                need += tank
                tank = 0
        
        return start if tank + need >= 0 else -1
