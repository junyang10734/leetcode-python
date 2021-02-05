# Longest Univalue Path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# faster than 17.84%
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            l_a, r_a = 0, 0
            if node.left and node.left.val == node.val:
                l_a = l + 1
            if node.right and node.right.val == node.val:
                r_a = r + 1
            self.ans = max(self.ans, l_a + r_a)
            return max(l_a, r_a)
        
        dfs(root)
        return self.ans


# Same with dfs
# faster than 34.86%
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.getPath(root)
        return self.res
        
    def getPath(self, node):
        if not node:
            return 0
        left = self.getPath(node.left)
        right = self.getPath(node.right)
        pl, pr = 0, 0
        if node.left and node.left.val == node.val:
            pl = left + 1
        if node.right and node.right.val == node.val:
            pr = right + 1
        self.res = max(self.res, pl + pr)
        return max(pl, pr)