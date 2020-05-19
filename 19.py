# Remove Nth Node From End of List
# Linked List / Two Points


# two pass
# runtime: faster than 65.88%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 0
        head1 = head
        while head1:
            i += 1
            head1 = head1.next
        
        dummy = ListNode(0)
        dummy.next = head
        
        head2 = dummy
        p = i - n
        while p > 0:
            p -= 1
            head2 = head2.next

        head2.next = head2.next.next
        
        return dummy.next



# one pass
# runtime: faster than 10.11%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy
        
        i = 0
        while i<n:
            first = first.next
            i += 1

        while first.next:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return dummy.next