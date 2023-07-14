# 1161. Maximum Level Sum of a Binary Tree
# Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        res = []
        while queue:
            n = len(queue)
            total = 0
            for i in range(n):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(total)
        
        index = -1
        s = -math.inf
        for i,n in enumerate(res):
            if n > s:
                s = n
                index = i
        return index+1
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node, level):
            if len(res) == level:
                res.append(0)
            res[level] += node.val
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
        
        dfs(root, 0)

        index, s = -1, -math.inf
        for i,num in enumerate(res):
            if num > s:
                s = num
                index = i
        return index+1