# Middle of the Linked List
# Linked List

# runtime: faster than 71.03%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        l, r = head, head
        
        while r and r.next:
            l = l.next
            r = r.next.next
        
        return l