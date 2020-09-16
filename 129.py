# Sum Root to Leaf Numbers
# Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS
# runtime: faster than 86.74%
# https://blog.csdn.net/fuxuemingzhu/article/details/79369956
class Solution1:
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


# Recursion
# faster than 7.26%
# https://www.cnblogs.com/zuoyuan/p/3721420.html
class Solution2:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.sum(root, 0)
    
    def sum(self, root, preSum):
        if not root:
            return 0
        preSum = preSum * 10 + root.val
        if not root.left and not root.right:
            return preSum
        return self.sum(root.left, preSum) + self.sum(root.right, preSum)
