# Minimum Depth of Binary Tree

# https://zxi.mytechroad.com/blog/tree/leetcode-111-minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# faster than 90.70%
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0 
        if not root.left and not root.right:
            return 1
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        
        if not root.left:
            return 1 + r
        if not root.right:
            return 1 + l
        
        return 1 + min(l, r)