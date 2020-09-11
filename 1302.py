# Deepest Leaves Sum

# https://blog.csdn.net/qq_17550379/article/details/103780463

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
# faster than 93.34%
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = [root]
        res = 0
        
        while q:
            res, n = 0, len(q)
            for i in range(n):
                cur = q.pop(0)
                res += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        
        return res