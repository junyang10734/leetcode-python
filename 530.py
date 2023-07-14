# 530. Minimum Absolute Difference in BST
# BST
# same as 783

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []

        def inorder(node):
            if node:
                inorder(node.left)
                arr.append(node.val)
                inorder(node.right)
        
        inorder(root)
        res = math.inf
        for a,b in zip(arr, arr[1:]):
            res = min(res, b-a)
        return res