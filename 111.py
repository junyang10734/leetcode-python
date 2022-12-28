# Minimum Depth of Binary Tree

# https://zxi.mytechroad.com/blog/tree/leetcode-111-minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# BFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        queue = collections.deque()
        queue.append(root)
        level = 1

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if not node.left and not node.right:
                    return level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        
        return level


# runtime: faster than 37.45%
class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0 
        if not root.left and not root.right:
            return 1
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        
        if not root.left:
            return 1 + r
        if not root.right:
            return 1 + l
        
        return 1 + min(l, r)


# runtime: faster than 59%
class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = float('inf')
        
        def dfs(node, depth):
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
            if not node.left and not node.right:
                self.res = min(self.res, depth)
        
        dfs(root, 1)
        return self.res