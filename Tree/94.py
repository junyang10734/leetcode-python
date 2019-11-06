# Binary Tree Inorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# recursive
# runtime: faster than 99.99% 
# space: less than 100.00% 
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def order(root):
            if root == None:
                return None
            if root.left != None:
                order(root.left)
            res.append(root.val)
            if root.right != None:
                order(root.right)
        
        order(root)
        return res


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
            
        return res