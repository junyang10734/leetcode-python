# 250. Count Univalue Subtrees
# DFS

# runtime: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.count = 0
        self.isUni(root)
        return self.count
    
    def isUni(self, node):
        if not node.left and not node.right:
            self.count += 1
            return True
        
        is_uni = True
        if node.left:
            is_uni = self.isUni(node.left) and node.left.val == node.val and is_uni
        if node.right:
            is_uni = self.isUni(node.right) and node.right.val == node.val and is_uni
        
        self.count += is_uni
        return is_uni