# Maximum Depth of Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# https://blog.csdn.net/fuxuemingzhu/article/details/48490829

# DFS
# faster than 42.80%
class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# BFS
# faster than 98.71%
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        d = 0
        que = collections.deque()
        que.append(root)
        
        while que:
            n = len(que)
            for i in range(n):
                node = que.popleft()
                if not node:
                    continue
                que.append(node.left)
                que.append(node.right)
            d += 1
        
        return d - 1