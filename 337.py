# House Robber III
# Tree / DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# https://blog.csdn.net/fuxuemingzhu/article/details/80779068

# DFS
# runtime: faster than 96.84%
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def dfs(root):
            if not root:
                return [0, 0]
            
            robleft = dfs(root.left)
            robright = dfs(root.right)
            norobcurr = robleft[1] + robright[1]
            robcurr = max(root.val + robleft[0] + robright[0], norobcurr)
            
            return [norobcurr, robcurr]
        
        return dfs(root)[1]
        