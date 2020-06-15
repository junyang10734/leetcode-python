# Swap Nodes in Pairs
# LinkedList

# https://blog.csdn.net/fuxuemingzhu/article/details/77678543
# runtime: faster than 59.77% 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root, root.next = self, head
        while root.next and root.next.next:
            a = root.next
            b = a.next
            root.next, a.next, b.next = b, b.next, a
            root = a
        return self.next