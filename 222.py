# Count Complete Tree Nodes
# Tree

# https://blog.csdn.net/fuxuemingzhu/article/details/80781666
# runtime: faster than 96.02%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        
        nodes = 0
        if left_height == right_height:
            nodes = 2 ** left_height + self.countNodes(root.right)
        else:
            nodes = 2 ** right_height + self.countNodes(root.left)
        
        return nodes

    
    def getHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height