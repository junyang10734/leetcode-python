# Palindrome Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
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