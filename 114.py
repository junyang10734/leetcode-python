# Flatten Binary Tree to Linked List
# Tree

# https://blog.csdn.net/fuxuemingzhu/article/details/70241424
# runtime: faster than 10.17% 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        self.preOrder(root, res)
        for i in range(len(res)-1):
            res[i].left = None
            res[i].right = res[i + 1]
        
        
    def preOrder(self, root, res):
        if not root:
            return
        res.append(root)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)
