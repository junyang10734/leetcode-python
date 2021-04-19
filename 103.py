# Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# BFS
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


# DFS
class Solution2:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        self.dfs(root, res, 0)
        for i,a in enumerate(res):
            if i % 2:
                res[i] = res[i][::-1]
        return res
    
    def dfs(self, node, res, d):
        if not node:
            return
        if d >= len(res):
            res.append([])
        res[d].append(node.val)
        self.dfs(node.left, res, d+1)
        self.dfs(node.right, res, d+1)