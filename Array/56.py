# Merge Intervals

# sort
# runtime: faster than 91.97% 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        res = []
        for i in intervals:
            if len(res) == 0 or i[0] > res[-1][1]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        
        return res                