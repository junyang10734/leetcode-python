# 1424. Diagonal Traverse II
# Array

# https://leetcode.com/problems/diagonal-traverse-ii/discuss/597794/Python-One-pass
# runtime: faster than 54.70%
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        for i,row in enumerate(nums):
            for j,num in enumerate(row):
                if len(res) <= i+j:
                    res.append([])
                res[i+j].append(num)
        return [n for r in res for n in reversed(r)]