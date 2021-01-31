# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Tree
# 类比105

# runtime: faster than 15.52%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return
        
        val = postorder[-1]
        index = inorder.index(val)
        
        root = TreeNode(val)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index: -1])
        
        return root