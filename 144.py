# Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# recursive
# runtime: faster than 35.68%
class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        
        def helper(root):
            if root == None:
                return None
            ans.append(root.val)
            if root.left != None:
                helper(root.left)
            if root.right != None:
                helper(root.right)
        
        helper(root)
        return ans


# stack, iterate
# runtime: faster than 5.98% 
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack = []
        ans = []
        stack.append(root)
        
        while stack:
            n = stack.pop()
            ans.append(n.val)
            if n.right != None:
                stack.append(n.right)
            if n.left != None:
                stack.append(n.left)
            
        return ans   
