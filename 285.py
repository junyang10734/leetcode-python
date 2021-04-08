# 285. Inorder Successor in BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# runtime: faster than 9.09%
class Solution1:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            left = dfs(node.left) if node.left else []
            right = dfs(node.right) if node.right else []
            return left + [node] + right
        
        arr = dfs(root)
        for i,a in enumerate(arr):
            if a == p and i < len(arr)-1:
                return arr[i+1]
        
        return None


# https://leetcode.com/problems/inorder-successor-in-bst/discuss/72656/JavaPython-solution-O(h)-time-and-O(1)-space-iterative
# runtime: faster than 97%
class Solution2:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor