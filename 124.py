# Binary Tree Maximum Path Sum
# Tree / DFS

# runtime: faster than 91.31%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://blog.csdn.net/qqxx6661/article/details/78484940
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float('-inf')
        self.getPathSum(root)
        return self.maxSum
    
    
    def getPathSum(self, root):
        if not root:
            return 0
        
        left = self.getPathSum(root.left)
        right = self.getPathSum(root.right)
        left = left if left > 0 else 0
        right = right if right > 0 else 0
        self.maxSum = max(self.maxSum, root.val + left + right)
        return max(left, right) + root.val