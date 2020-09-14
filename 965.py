# Univalued Binary Tree
# https://blog.csdn.net/fuxuemingzhu/article/details/85385974


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
# faster than 5.16% 
class Solution1:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        q = collections.deque()
        q.append(root)
        val = root.val
        
        while q:
            node = q.popleft()
            if not node:
                continue
            if node.val != val:
                return False
            q.append(node.left)
            q.append(node.right)
            
        return True



# DFS
# faster than 86.89%
class Solution2:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.dfs(root, root.val)
    
    def dfs(self, node, val):
        if not node:
            return True
        if node.val != val:
            return False
        return self.dfs(node.left, val) and self.dfs(node.right, val)