# 725. Split Linked List in Parts

# https://leetcode.com/problems/split-linked-list-in-parts/solutions/109284/elegant-python-with-explanation/?envType=daily-question&envId=2023-09-06

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr, length  = head, 0
        while curr:
            length += 1
            curr = curr.next
            
        chunkSize = length // k
        longerChunk = length % k
        res = [chunkSize + 1] * longerChunk + [chunkSize] * (k - longerChunk)

        prev, curr = None, head
        for idx, num in enumerate(res):
            if prev:
                prev.next = None
            res[idx] = curr
            for i in range(num):
                prev, curr = curr, curr.next
        return res
                
        