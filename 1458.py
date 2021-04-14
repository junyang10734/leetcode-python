# 1485. Clone Binary Tree With Random Pointer
# Tree

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/solution/
class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return 
        
        d = {}
        stack = [root]
        
        while stack:
            node = stack.pop(0)
            d[node] = NodeCopy(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left:
                d[node].left = d[node.left]
                stack.append(node.left)
            if node.right:
                d[node].right = d[node.right]
                stack.append(node.right)
            if node.random:
                d[node].random = d[node.random]
        
        return d[root]
                        