# 366. Find Leaves of Binary Tree
# Tree / DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# postOrder
# https://leetcode.com/problems/find-leaves-of-binary-tree/solution/
# runtime: O(n)
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(list)
        
        def dfs(node, height):
            if not node:
                return height
            left = dfs(node.left, height)
            right = dfs(node.right, height)
            height = max(left, right)
            d[height].append(node.val)
            return height + 1
        
        dfs(root, 0)
        return d.values()
        