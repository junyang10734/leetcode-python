# 116. Populating Next Right Pointers in Each Node
# Tree 递归

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


# reference: https://blog.csdn.net/fuxuemingzhu/article/details/79559645
# runtime: faster than 98.51%
class Solution1:
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


# labuladong
# runtime: faster than 5.00%
class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        self.connectTwoNodes(root.left, root.right)
        return root
        
    
    def connectTwoNodes(self, node1, node2):
        if not node1 or not node2:
            return    
        node1.next = node2
        self.connectTwoNodes(node1.left, node1.right)
        self.connectTwoNodes(node2.left, node2.right)
        self.connectTwoNodes(node1.right, node2.left)