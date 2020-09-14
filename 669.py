# Trim a Binary Search Tree
# Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursion
# runtime: faster than 43.28% 
# https://leetcode.com/problems/trim-a-binary-search-tree/solution/
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
        
        return trim(root)


# Recursion
# https://blog.csdn.net/fuxuemingzhu/article/details/83869684
# faster than 70.88%
class Solution2:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        if root.val > high:
            return self.trimBST(root.left, low, high)
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
