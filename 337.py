# House Robber III
# 打家劫舍问题：198, 213, 337
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
class Solution1:
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
class Solution2:
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
        


# labuladong
# DP
# runtime: faster than 76.40%
class Solution3:
    d = {}
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        if root in self.d:
            return self.d[root]
        
        robcurr = root.val + (0 if not root.left else (self.rob(root.left.left) + self.rob(root.left.right))) + (0 if not root.right else (self.rob(root.right.left) + self.rob(root.right.right)))
        norobcurr = self.rob(root.left) + self.rob(root.right)
        res = max(robcurr, norobcurr)
        self.d[root] = res
        
        return res