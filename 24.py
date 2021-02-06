# Swap Nodes in Pairs
# LinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://maxming0.github.io/2020/12/28/Swap-Nodes-in-Pairs/
# runtime: faster than 59.77% 
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy, dummy.next = ListNode(), head
        res = dummy
        while dummy.next and dummy.next.next:
            a = dummy.next
            b = a.next
            dummy.next, b.next, a.next = b, a, b.next
            dummy = a
        return res.next