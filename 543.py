# Diameter of Binary Tree
# Tree

# runtime: faster than 89.43%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# DFS + Recursion
# faster than 92.98%
class Solution1:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def depth(node):
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            self.ans = max(self.ans, l+r+1)
            return max(l,r) + 1
        
        depth(root)
        return self.ans - 1