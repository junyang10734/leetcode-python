# Vertical Order Traversal of a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# https://blog.csdn.net/fuxuemingzhu/article/details/87829987

# DFS
# runtime: faster than 93.61%
class Solution1:
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
           
    def dfs(self, node, x, y):
        if not node:
            return 
        self.m.append((x, y, node.val))
        self.dfs(node.left, x-1, y+1)
        self.dfs(node.right, x+1, y+1)


# BFS
# runtime: faster than 91.46% 
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