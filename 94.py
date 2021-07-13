# Binary Tree Inorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS
# recursive
# runtime: faster than 99.99% 
# space: less than 100.00% 
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def inOrder(node):
            if not node:
                return None
            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)
        
        inOrder(root)
        return res


# BFS
# stack, iterate
# runtime: faster than 98.77% 
# space: less than 100.00% 
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            root = stack.pop()
            res.append(root.val)
            root = root.right
            
