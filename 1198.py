# 1198. Find Smallest Common Element in All Rows
# Hash Table

# runtime: faster than 51%
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        for m in mat:
            for i in m:
                d[i] +=1
        
        res = []
        for k,v in d.items():
            if v == len(mat):
                res.append(k)
        res.sort()
        return res[0] if len(res) > 0 else -1