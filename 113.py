# 113. Path Sum II

# DFS / backtrack
# faster than 84.56%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        def dfs(node, s, path):
            if not node.left and not node.right:
                if node.val + s == targetSum:
                    res.append(path + [node.val])
            else:
                if node.left:
                    dfs(node.left, node.val + s, path + [node.val])
                if node.right:
                    dfs(node.right, node.val + s, path + [node.val])
        
        dfs(root, 0, [])
        return res