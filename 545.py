# 545. Boundary of Binary Tree
# Tree

# runtime: faster than 41.42%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# BFS to find left boundary and right boundary
# DFS to find leaves
# runtime: faster than 41.42%
class Solution1:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root.left and not root.right:
            return [root.val]
        
        left, right, leaves = [], [], []
        
        q = collections.deque([(root,0)])
        while q:
            tmp = q.popleft()
            node, flag = tmp[0], tmp[1]
            if node:
                if flag == -1 and (node.left or node.right):
                    left.append((node.val))
                    if node.left:
                        q.append((node.left, -1))
                    elif node.right:
                        q.append((node.right, -1))
                elif flag == 1 and (node.left or node.right):
                    right.append((node.val))
                    if node.right:
                        q.append((node.right, 1))
                    elif node.left:
                        q.append((node.left, 1))
                elif flag == 0 and (node.left or node.right):
                    if node.left:
                        q.append((node.left, -1))
                    if node.right:
                        q.append((node.right, 1))
                        
        
        def dfs(node):
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        return [root.val] + left + leaves + right[::-1]


# DFS
# runtime: faster than 69.71%
class Solution2:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root.left and not root.right:
            return [root.val]
        
        left, right, leaves = [], [], []
        def getLeft(node):
            if node and (node.left or node.right):
                left.append(node.val)
                if node.left:
                    getLeft(node.left)
                else:
                    getLeft(node.right)
        
        def getRight(node):
            if node and (node.left or node.right):
                right.append(node.val)
                if node.right:
                    getRight(node.right)
                else:
                    getRight(node.left)
        
        def getLeaf(node):
            if node and not node.left and not node.right:
                leaves.append(node.val)
            else:
                if node.left:
                    getLeaf(node.left)
                if node.right:
                    getLeaf(node.right)
        
        getLeft(root.left)
        getRight(root.right)
        getLeaf(root)
        return [root.val] + left + leaves + right[::-1]