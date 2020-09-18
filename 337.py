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


# DFS
# faster than 43.77% 
class Solution:
    def rob(self, root: TreeNode) -> int:
        self.d = {}
        return self.helper(root, False)
    
    def helper(self, node, parentUsed):
        if not node:
            return 0
        if (node, parentUsed) in self.d:
            return self.d[(node, parentUsed)]
        res = 0
        if parentUsed:
            res = self.helper(node.left, False) + self.helper(node.right, False)
        else:
            res = max(node.val + self.helper(node.left, True) + self.helper(node.right, True), self.helper(node.left, False) + self.helper(node.right, False))
        
        self.d[(node, parentUsed)] = res
        return res
        