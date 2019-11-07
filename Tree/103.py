# Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# runtime: faster than 97.93%
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        cur_level = [root]
        zigzag = True
        while cur_level:
            res.append([node.val for node in cur_level])
            next_level = []
            
            if zigzag:
                cur_level = cur_level[::-1]
                for node in cur_level:
                    if node.right:
                        next_level.append(node.right)
                    if node.left:
                        next_level.append(node.left)
            else:
                cur_level = cur_level[::-1]
                for node in cur_level:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
            
                
            zigzag = not(zigzag)
            cur_level = next_level
        
        return res