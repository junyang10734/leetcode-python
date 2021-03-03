# 1629. Slowest Key
# Array

# runtime: faster than 73.32%
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res = keysPressed[0]
        mx = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            diff = releaseTimes[i] - releaseTimes[i-1]
            if diff == mx:
                res = max(res, keysPressed[i])
            elif diff > mx:
                mx, res = diff, keysPressed[i]
        return res