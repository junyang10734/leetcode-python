# Binary Tree Pruning

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# postOrder / Recursion
# https://blog.csdn.net/fuxuemingzhu/article/details/79858752
# faster than 8.40%
class Solution1:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and not root.left and not root.right:
            return None
        return root


# Recursion
# https://leetcode.com/problems/binary-tree-pruning/solution/
# faster than 46.39% 
class Solution2:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def containsOne(node):
            if not node:
                return False
            a1 = containsOne(node.left)
            a2 = containsOne(node.right)
            if not a1:
                node.left = None
            if not a2:
                node.right = None
            return node.val == 1 or a1 or a2
        
        return root if containsOne(root) else None