# 1776. Car Fleet II
# Stack

# https://leetcode.com/problems/car-fleet-ii/discuss/1085987/JavaC%2B%2BPython-O(n)-Stack-Solution
# runtime: O(n)
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        stack = []
        res = [-1]*n
        
        for i in range(n-1, -1, -1):
            p, s = cars[i]
            while stack and (s <= cars[stack[-1]][1] or (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1]) >= res[stack[-1]] > 0):
                stack.pop()
            
            if stack:
                res[i] = (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1])
            
            stack.append(i)
        
        return res
