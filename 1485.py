# 1485. Clone Binary Tree With Random Pointer
# BFS

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return
        
        d = {}
        q = collections.deque([root])
        while q:
            node = q.popleft()
            d[node] = NodeCopy(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.left:
                d[node].left = d[node.left]
                q.append(node.left)
            if node.right:
                d[node].right = d[node.right]
                q.append(node.right)
            if node.random:
                d[node].random = d[node.random]
        
        return d[root]
                