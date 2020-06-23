# 445. Add Two Numbers II
# Linked List

# https://blog.csdn.net/fuxuemingzhu/article/details/79380457

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# runtime: faster than 99.54%
class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = '', ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
            
        _sum = str(int(num1) + int(num2))
        head = ListNode(_sum[0])
        ans = head
        for i in range(1, len(_sum)):
            node = ListNode(_sum[i])
            head.next = node
            head = head.next
        
        return ans


# Stack
# runtime: faster than 85.24% 
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        ans = None
        carry = 0
        
        while stack1 and stack2:
            add = stack1.pop() + stack2.pop() + carry
            carry = 1 if add >= 10 else 0
            temp = ans
            ans = ListNode(add % 10)
            ans.next = temp
        
        l = stack1 if stack1 else stack2
        while l:
            add = l.pop() + carry
            carry = 1 if add >= 10 else 0
            temp = ans
            ans = ListNode(add % 10)
            ans.next = temp
        
        if carry:
            temp = ans
            ans = ListNode(1)
            ans.next = temp
        
        return ans