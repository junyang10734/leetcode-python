# Sum Root to Leaf Numbers
# Tree

# https://blog.csdn.net/fuxuemingzhu/article/details/79369956
# runtime: faster than 86.74%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        res = [0]
        self.dfs(root, res, root.val)
        return res[0]
    
    def dfs(self, root, res, path):
        if root.left == None and root.right == None:
            res[0] += path
        if root.left != None:
            self.dfs(root.left, res, path * 10 + root.left.val)
        if root.right != None:
            self.dfs(root.right, res, path * 10 + root.right.val)
