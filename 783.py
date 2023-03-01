# 783. Minimum Distance Between BST Nodes
# BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []

        def inorder(node):
            if node:
                inorder(node.left)
                arr.append(node.val)
                inorder(node.right)
        
        inorder(root)

        res = math.inf
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < res:
                res = arr[i+1] - arr[i]
        return res