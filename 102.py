# Binary Tree Level Order Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: faster than 99.45%
# https://github.com/criszhou/LeetCode-Python/blob/master/102.%20Binary%20Tree%20Level%20Order%20Traversal.py
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        cur_level = [root]
        
        while cur_level:
            res.append([ node.val for node in cur_level])
            
            next_level = []
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            cur_level = next_level
        
        return res