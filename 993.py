# Cousins in Binary Tree
# Tree

# https://blog.csdn.net/fuxuemingzhu/article/details/87867902

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS
# runtime: faster than 64.35%
class Solution1:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.m = collections.defaultdict(tuple)
        self.dfs(root, None, 0)
        px, dx = self.m[x]
        py, dy = self.m[y]
        return dx == dy and px != py
    
    def dfs(self, root, parent, depth):
        if not root:
            return
        self.m[root.val] = (parent, depth)
        self.dfs(root.left, root, depth+1)
        self.dfs(root.right, root, depth+1)