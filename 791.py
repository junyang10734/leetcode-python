# 791. Custom Sort String
# Sorting / Hash Table

class Solution:
    def customSortString(self, order: str, str: str) -> str:
        d1 = {}  # order of char in order
        for i,c in enumerate(order):
            d1[c] = i
        
        d2 = {} # frequency of char in str which appear in order
        d3 = {} # frequency of char in str which not appear in order
        for c in str:
            if c in d1:
                d2[c] = d2.get(c, 0) + 1
            else:
                d3[c] = d3.get(c, 0) + 1
        
        res = ''
        for k,v in sorted(d1.items(), key=lambda x:x[1]):
            if k in d2:
                res += k * d2[k]
        for k,v in d3.items():
            res += k * v
        return res
        