# 142 Linked List Cycle II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# two pointers
# runtime: faster than 76.89%
# https://blog.csdn.net/fuxuemingzhu/article/details/79530638
class Solution1:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast


# hash map
# run time: faster than 76.89%
# https://leetcode.com/problems/linked-list-cycle-ii/discuss/498204/Python-Hashmap
class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        dic = {}
        while head:
            dic[head] = head
            if dic.get(head.next, 0):
                return head.next
            head = head.next