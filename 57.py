# 57. Insert Interval
# Array

# https://leetcode.com/problems/insert-interval/solutions/21809/python-o-n-and-o-nlgn-solutions/?orderBy=most_votes
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i,item in enumerate(intervals):
            if item[1] < newInterval[0]:
                res.append(item)
            elif newInterval[1] < item[0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                # overlap
                newInterval[0] = min(newInterval[0], item[0])
                newInterval[1] = max(newInterval[1], item[1])

        res.append(newInterval)
        
        return res
