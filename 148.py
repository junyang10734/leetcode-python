# Sort List
# Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# https://zxi.mytechroad.com/blog/divide-and-conquer/leetcode-148-sort-list/
# runtime: faster than 53.96%
class Solution1:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(l1, l2):
            dummy = ListNode(0)
            tail = dummy
            while l1 and l2:
                if l1.val > l2.val: l1, l2 = l2, l1
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            return dummy.next
    
        if not head or not head.next: return head
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        return merge(self.sortList(head), self.sortList(mid))


# 先将node存入list，对list排序，最后将排序后的list构建链表
# runtime: faster than 91.42%
class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        l = []    
        while head:
            l.append(head.val)
            head = head.next
        
        l.sort()
        head = node = ListNode(l[0])
        if len(l) == 1:
            node.next = None
            return node
        else:
            for i in range(1, len(l)):
                newNode = ListNode(l[i])
                node.next = newNode
                node = newNode
            node.next = None
            return head