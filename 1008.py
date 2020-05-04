# Construct Binary Search Tree from Preorder Traversal
# Tree

# https://blog.csdn.net/fuxuemingzhu/article/details/88379241
# runtime: faster than 99.60%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        
        count = len(preorder)
        i = 1
        while i<count:
            if preorder[i] > preorder[0]:
                break
            i += 1
        
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        
        
        return root