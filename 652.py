# 652. Find Duplicate Subtrees
# Tree
# DFS 递归 + 序列化


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://blog.csdn.net/fuxuemingzhu/article/details/81053453
# runtime: faster than 22.04%
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res = []
        d = collections.defaultdict(int)
        self.helper(res, root, d)
        return res
    
    def helper(self, res, node, d):
        if not node:
            return '#'
        
        path = str(node.val) + ',' + self.helper(res, node.left, d) + ',' + self.helper(res, node.right, d)
        
        if d[path] == 1:
            res.append(node)
        d[path] += 1
        
        return path
        