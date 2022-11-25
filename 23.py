# 23. Merge k Sorted Lists
# Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 将所有结点存入数组，数组排序，再生成Linked List
# runtime: faster than 97.92%
class Solution1:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        arr = []
        for l in lists:
            while l:
                arr.append(l.val)
                l = l.next
        
        if len(arr) == 0:
            return None
        
        arr.sort()   
        head = node = ListNode(arr[0])
        for i in range(1, len(arr)):
            newNode = ListNode(arr[i])
            node.next = newNode
            node = newNode
        
        return head


# Heap
# runtime: faster than 76.42%
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i,head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        dummy = current = ListNode(-1)
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next