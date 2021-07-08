# 364. Nested List Weight Sum II
# Hash Table

# https://leetcode.com/problems/nested-list-weight-sum-ii/discuss/156579/Python-100-w-Dictionary
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        depth, res, d = 1, 0, {}
        while nestedList:
            d[depth] = [x.getInteger() for x in nestedList if x.isInteger()]
            nestedList = sum([x.getList() for x in nestedList if not x.isInteger()], [])
            depth += 1
        
        for k,v in d.items():
            res += (depth - k) * sum(v)
        return res