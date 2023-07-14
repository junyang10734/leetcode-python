# 783. Minimum Distance Between BST Nodes
# BST
# same as 530

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
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def helper(node, high, low):
            if not node:
                return high - low
            left = helper(node.left, node.val, low)
            right = helper(node.right, high, node.val)
            return min(left, right)
        
        return helper(root, math.inf, -math.inf)