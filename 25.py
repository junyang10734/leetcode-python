# 25. Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative
# https://labuladong.gitbook.io/algo/shu-ju-jie-gou-xi-lie/shou-ba-shou-shua-lian-biao-ti-mu-xun-lian-di-gui-si-wei/k-ge-yi-zu-fan-zhuan-lian-biao
# runtime: faster than 79.99%
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        
        a = b = head
        i = 0
        while i < k:
            if not b:
                return head
            b = b.next
            i += 1
        
        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead
        
        
    def reverse(self, first, last):
        pre, cur, nxt = None, first, first
        
        while cur != last:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre
        