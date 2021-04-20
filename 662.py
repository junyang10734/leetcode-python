# 662. Maximum Width of Binary Tree
# DFS / BFS

# https://leetcode.com/problems/maximum-width-of-binary-tree/solution/
# DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        index = {}
        count = 0
        
        def dfs(node, depth, col):
            nonlocal count
            if not node:
                return
            if depth not in index:
                index[depth] = col
            count = max(count, col-index[depth]+1)
            dfs(node.left, depth+1, 2*col)
            dfs(node.right, depth+1, 2*col+1)
        
        dfs(root, 0, 0)
        return count