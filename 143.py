# Reorder List
# Linked List

# https://blog.csdn.net/fuxuemingzhu/article/details/80805434
# runtime: faster than 55.33%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            fast, slow = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            head1 = head
            head2 = slow.next
            slow.next = None  
        
            dummy = ListNode(0)
            dummy.next = head2
            p = head2.next
            head2.next = None
            while p:
                temp = p
                p = p.next
                temp.next = dummy.next
                dummy.next = temp
            head2 = dummy.next    

            p1 = head1
            p2 = head2
            while p2:
                temp1 = p1.next
                temp2 = p2.next
                p1.next = p2
                p2.next = temp1
                p1 = temp1
                p2 = temp2