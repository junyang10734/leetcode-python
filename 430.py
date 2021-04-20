# 430. Flatten a Multilevel Doubly Linked List

# DFS

# https://blog.csdn.net/fuxuemingzhu/article/details/81985172
# runtime: faster than 17.94%
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

# DFS + recursive
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        node = head
        while node:
            if node.child:
                flattened = self.flatten(node.child)
                node.child = None
                nextNode = self.appendToList(node, flattened)
                node = nextNode
            else:
                node = node.next
        return head
    
    def appendToList(self, node, l):
        nextNode = node.next
        node.next = l
        l.prev = node
        while node.next:
            node = node.next
        node.next = nextNode
        if nextNode:
            nextNode.prev = node
        return nextNode
        

# DFS + Iteration
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/solution/
class Solution2:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        
        pHead = Node(0, None, head, None)
        prev = pHead
        stack = [head]
        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        
        pHead.next.prev = None
        return pHead.next