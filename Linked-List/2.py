# Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# recursive
# runtime: faster than 17.70%
class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        sum_val = l1.val + l2.val
        if sum_val < 10:
            node = ListNode(sum_val)
            node.next = self.addTwoNumbers(l1.next, l2.next)
            return node
        else:
            q = sum_val - 10
            node = ListNode(q)
            node.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
            return node


# runtime: faster than 33.60%
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        res_tail = res
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, out = divmod(val1+val2+carry, 10)
            
            res_tail.next = ListNode(out)
            res_tail = res_tail.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next