# 1214. Two Sum BSTs
# Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        s1 = set()
        s2 = set()
        def dfs(node, s):
            if node:
                s.add(node.val)
                dfs(node.left, s)
                dfs(node.right, s)
        
        dfs(root1, s1)
        dfs(root2, s2)

        for num in s1:
            if (target - num) in s2:
                return True

        return False