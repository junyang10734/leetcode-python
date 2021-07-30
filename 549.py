# 549. Binary Tree Longest Consecutive Sequence II
# DFS

# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/discuss/389210/Python-bottom-up-DFS-solution-(56-ms-beat-93.37)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(node):
            if not node:
                return 0, 0
            
            inc, dec = 1, 1
            li, ld = dfs(node.left)
            ri, rd = dfs(node.right)
            
            if node.left:
                if node.left.val == node.val + 1:
                    inc = max(inc, 1 + li)
                elif node.left.val == node.val - 1:
                    dec = max(dec, 1 + ld)
            if node.right:
                if node.right.val == node.val + 1:
                    inc = max(inc, 1 + ri)
                elif node.right.val == node.val - 1:
                    dec = max(dec, 1 + rd)
            
            self.res = max(self.res, inc + dec - 1)
            return inc, dec
        
        dfs(root)
        return self.res