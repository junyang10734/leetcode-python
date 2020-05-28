# Lowest Common Ancestor of a Binary Tree
# Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursive Approach
# runtime: faster than 82.31% 
class Solution1:
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recurse_tree(current_node):
            if not current_node:
                return False
            
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            mid = current_node == p or current_node == q
            
            if mid + left + right >= 2:
                self.ans = current_node
            
            return mid or left or right
        
        recurse_tree(root)
        
        return self.ans
            


# Iterative using parent pointers
# runtime: faster than 82.31% 
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root] 
        parent = {root: None}
        
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
        
        return q