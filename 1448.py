# 1448. Count Good Nodes in Binary Tree
# DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 0
        
        def dfs(node, maxV):
            if node.val >= maxV:
                self.res += 1
            maxV = max(node.val, maxV)
            if node.left:
                dfs(node.left, maxV)
            if node.right:
                dfs(node.right, maxV)
            
        dfs(root, -inf)
        return self.res