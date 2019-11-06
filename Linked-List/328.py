# Odd Even Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# runtime: O(n) faster than 51.08% 
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        else:
            odd = head
            even = head.next
            head2 = even
            while odd.next != None and even.next != None:
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next
            odd.next = head2
            return head