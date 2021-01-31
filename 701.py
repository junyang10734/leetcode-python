# 701. Insert into a Binary Search Tree
# Tree 递归

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# runtime: faster than 83.73%
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if root.val < val:
            if root.right:
                root.right = self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        elif root.val > val:
            if root.left:
                root.left = self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
                
        return root