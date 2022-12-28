# 1026. Maximum Difference Between Node and Ancestor
# Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        maxv = root.val
        minv = root.val

        def helper(node, maxv, minv):
            self.res = max(self.res, abs(node.val - maxv), abs(node.val - minv))
            maxv = max(maxv, node.val)
            minv = min(minv, node.val)
            if node.left:
                helper(node.left, maxv, minv)
            if node.right:
                helper(node.right, maxv, minv)

        
        helper(root, maxv, minv)
        return self.res
