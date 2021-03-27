# 759. Employee Free Time
# Array


# https://leetcode.com/problems/employee-free-time/solution/

# Line Sweep
# runtime: faster than 59.86%
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = []
        for s in schedule:
            for item in s:
                events.append((item.start, 0))
                events.append((item.end, 1))
        events.sort()
        res = []
        prev = float('-inf')
        balance = 0
        for t,state in events:
            if balance == 0 and prev >= 0:
                res.append(Interval(prev, t))
            balance += 1 if not state else -1
            prev = t
        return res