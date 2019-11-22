"""
Given a BST and its root, find the minimum path sum from root to leaves.
Only need to return sum, do not need to return path.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minPathSum(root):
    if root is None:
        return 0
    elif root.left is not None and root.right is None:
        return minPathSum(root.left) + root.val
    elif root.right is not None and root.left is None:
        return minPathSum(root.right) + root.cal
    else:
        return min(minPathSum(root.left), minPathSum(root.right)) + root.val
