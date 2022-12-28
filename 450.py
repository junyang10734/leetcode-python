# 450. Delete Node in a BST
# Tree 递归

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# runtime: faster than 32.88%
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return 
        
        if key == root.val:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.getMin(root.right)
                root.right = self.deleteNode(root.right, minNode.val)
                minNode.left = root.left
                minNode.right = root.right
                root = minNode
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        return root
    
    def getMin(self, node):
        while node.left:
            node = node.left
        return node