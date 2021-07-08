# 339. Nested List Weight Sum
# DFS

# https://leetcode.com/problems/nested-list-weight-sum/solution/
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            total = 0
            for x in nestedList:
                if x.isInteger():
                    total += x.getInteger() * depth
                else:
                    total += dfs(x.getList(), depth+1)
            return total
             
        return dfs(nestedList, 1)