# Merge Intervals

# sort
# runtime: faster than 23.77% 
class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        res = []
        for i in intervals:
            if len(res) == 0 or i[0] > res[-1][1]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        
        return res                


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for invt in intervals[1:]:
            last = res[-1]
            if invt[0] <= last[1]:
                last[1] = max(last[1], invt[1])
            else:
                res.append(invt)
        
        return res


# https://blog.csdn.net/fuxuemingzhu/article/details/69078468
# running time: faster than 99.24% 
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        N = len(intervals)
        if not N:
            return []
        
        intervals.sort(key=lambda x:x[0])
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for item in intervals:
            if item[0] <= end:
                end = max(end, item[1])
            else:
                cur = [start, end]
                res.append(cur)
                start = item[0]
                end = item[1]
                
        res.append([start, end])
        return res