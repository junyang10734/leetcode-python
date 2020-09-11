# Vertical Order Traversal of a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# https://blog.csdn.net/fuxuemingzhu/article/details/87829987

# DFS
# runtime: faster than 45.51%
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.m = []
        self.dfs(root, 0, 0)
        self.m.sort()
        res = [[self.m[0][2]]]
        for i in range(1, len(self.m)):
            if self.m[i][0] == self.m[i-1][0]:
                res[-1].append(self.m[i][2])
            else:
                res.append([self.m[i][2]])
                
        return res
    
    def dfs(self, root, x, y):
        if not root:
            return 
        self.m.append((x, -y, root.val))
        self.dfs(root.left, x-1, y-1)
        self.dfs(root.right, x+1, y-1)


# BFS
# faster than 91.46% 
class Solution2:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        q = collections.deque()
        q.append((root, 0, 0))
        m = []
        
        while q:
            node, x, y = q.popleft()
            m.append((x, -y, node.val))
            if node.left:
                q.append((node.left, x-1, y-1))
            if node.right:
                q.append((node.right, x+1, y-1))
            
        m.sort()
        res = [[m[0][2]]]
        for i in range(1, len(m)):
            if m[i][0] == m[i-1][0]:
                res[-1].append(m[i][2])
            else:
                res.append([m[i][2]])
        
        return res