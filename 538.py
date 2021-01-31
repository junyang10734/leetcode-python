# 538. Convert BST to Greater Tree
# Tree 
# same as 1038

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 后续遍历 + 维护一个sum值
# runtime: faster than 93.81%
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.s = 0
        
        def postOrder(node):
            if not node:
                return 
            postOrder(node.right)
            self.s += node.val
            node.val = self.s
            postOrder(node.left)
            
        postOrder(root)
        return root