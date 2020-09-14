# Binary Tree Level Order Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: faster than 99.45%
# https://github.com/criszhou/LeetCode-Python/blob/master/102.%20Binary%20Tree%20Level%20Order%20Traversal.py
class Solution1:
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


# DFS
# faster than 98.88%
# https://blog.csdn.net/fuxuemingzhu/article/details/49102937
class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.getLevel(root, res, 0)
        return res
        
    def getLevel(self, node, res, d):
        if not node:
            return
        if d >= len(res):
            res.append([])
        res[d].append(node.val)
        self.getLevel(node.left, res, d+1)
        self.getLevel(node.right, res, d+1)


# BFS
# faster than 19.11%
# https://blog.csdn.net/fuxuemingzhu/article/details/49102937
class Solution3s:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        q = collections.deque()
        q.append(root)
        
        while q:
            level = []
            size = len(q)
            
            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        
        return res