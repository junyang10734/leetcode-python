# 234. Palindrome Linked List
# Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Array
# runtime: faster than 59.93%
class Solution1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        l = []
        while head != None:
            l.append(head.val)
            head = head.next

        return l == l[::-1]


# recursive / stack
# https://labuladong.gitbook.io/algo/shu-ju-jie-gou-xi-lie/shou-ba-shou-shua-lian-biao-ti-mu-xun-lian-di-gui-si-wei/pan-duan-hui-wen-lian-biao
# runtime: faster than 59.93%
class Solution2:
    left = None
    
    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head
        return self.traverse(head)
    
    def traverse(self, right):
        if not right:
            return True
        res = self.traverse(right.next)
        res = res and right.val == self.left.val
        self.left = self.left.next
        return res