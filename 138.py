# 138. Copy List with Random Pointer
# Hash Table / Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# https://blog.csdn.net/fuxuemingzhu/article/details/80787528
# runtime: faster than 69.85% 
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = {}
        dummy = Node(0, None, None)
        d[head] = dummy
        newHead, pointer = dummy, head
        while pointer:
            node = Node(pointer.val, pointer.next, None)
            d[pointer] = node
            newHead.next = node
            newHead, pointer = newHead.next, pointer.next
        pointer = head
        while pointer:
            if pointer.random:
                d[pointer].random = d[pointer.random]
            pointer = pointer.next
        
        return dummy.next
