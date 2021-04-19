# 86. Partition List
# Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        
        after.next = None
        before.next = after_head.next
        return before_head.next


class Solution2:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return
        
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next

        arr1, arr2 = [], []
        for a in arr:
            if a < x:
                arr1.append(a)
            else:
                arr2.append(a)
        arr = arr1 + arr2
        
        head = ListNode(arr[0])
        node = head
        for i in range(1, len(arr)):
            node.next = ListNode(arr[i])
            node = node.next
        return head