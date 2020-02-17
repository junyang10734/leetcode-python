# Populating Next Right Pointers in Each Node

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# runtime: faster than 98.51% of Python3
# reference: https://blog.csdn.net/fuxuemingzhu/article/details/79559645
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        if root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root