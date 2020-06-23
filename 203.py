# Remove Linked List Elements
# Linked List

# runtime: faster than 63.17%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        root = ListNode(-1)
        root.next = head
        pre = root
        cur = head
        
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return root.next
            
