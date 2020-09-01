# Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
# runtime: faster than 5.99%
class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        
        def helper(root):
            if not root:
                return None
            if root.left != None:
                helper(root.left)
            if root.right != None:
                helper(root.right)
            ans.append(root.val)
        
        helper(root)
        return ans

# stack, iterate
# runtime: faster than 9.76% 
class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack = []
        ans = []
        stack.append(root)
        
        while stack:
            n = stack.pop()
            if n:
                ans.append(n.val)
                stack.append(n.left)
                stack.append(n.right)
        
        return ans[::-1]