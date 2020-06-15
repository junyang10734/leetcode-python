# Search in a Binary Search Tree
# Tree

# runtime: faster than 99.44% 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val < val:
            root = root.right
            return self.searchBST(root, val)
        elif root.val == val:
            return root
        else:
            root = root.left
            return self.searchBST(root, val)
            