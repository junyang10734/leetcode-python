# 270. Closest Binary Search Tree Value
# Tree / BST / Binary Search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/closest-binary-search-tree-value/solution/

# BST
# runtime: O(H)
class Solution1:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            if abs(target - root.val) < abs(target - closest):
                closest = root.val
            root = root.left if target < root.val else root.right
        return closest


# inorder
# runtime: O(N)
class Solution2:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        return min(inorder(root), key=lambda x: abs(target - x))