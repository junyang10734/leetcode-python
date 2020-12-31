# 1145. Binary Tree Coloring Game
# Tree

# https://blog.csdn.net/qq_32424059/article/details/98455253
# running time: faster than 74.09%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.x_addr = 0
        
        def dfs(node):
            if not node:
                return
            if node.val == x:
                self.x_addr = node
                return 
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        
        
        def countOfSubtree(node):
            if not node:
                return 0
            return 1 + countOfSubtree(node.left) + countOfSubtree(node.right)
        
        
        if root.val == x:
            return countOfSubtree(root.left) != countOfSubtree(root.right)
        else:
            total_count = countOfSubtree(root)
            x_count = countOfSubtree(self.x_addr)
            left_count = countOfSubtree(self.x_addr.left)
            right_count = countOfSubtree(self.x_addr.right)
            
            return x_count < total_count - x_count or left_count > total_count - left_count or right_count > total_count - right_count