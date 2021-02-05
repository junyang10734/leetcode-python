# 92. Reverse Linked List II
# Linked List 反转链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Recursive
# https://labuladong.gitbook.io/algo/shu-ju-jie-gou-xi-lie/shou-ba-shou-shua-lian-biao-ti-mu-xun-lian-di-gui-si-wei/di-gui-fan-zhuan-lian-biao-de-yi-bu-fen
# runtime: faster than 87.25%
class Solution1:
    successor = None
    
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseN(head, n)
        else:
            head.next = self.reverseBetween(head.next, m-1, n-1)
            return head
        
    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return last


# Iterative
# https://blog.csdn.net/fuxuemingzhu/article/details/80794665
# runtime: faster than 66.76%
class Solution2:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        count = 1
        root = ListNode(0)
        root.next = head
        prev = root
        
        while prev.next and count < m:
            prev = prev.next
            count += 1
        
        if count < m:
            return head
        
        tmp = prev.next
        curr = tmp.next
        while curr and count < n:
            third = curr.next
            curr.next = prev.next
            prev.next = curr
            tmp.next = third
            curr = third
            count += 1
        
        return root.next