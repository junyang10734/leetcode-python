# Path Sum II

# https://blog.csdn.net/fuxuemingzhu/article/details/80779723

# DFS / backtrack
# faster than 84.56%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.dfs(root, res, sum, [root.val])
        return res
    
    def dfs(self, root, res, target, path):
        if not root:
            return 
        if target == sum(path) and not root.left and not root.right:
            res.append(path)
            return
        if root.left:
            self.dfs(root.left, res, target, path + [root.left.val])
        if root.right:
            self.dfs(root.right, res, target, path + [root.right.val])