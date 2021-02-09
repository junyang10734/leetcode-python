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
# https://blog.csdn.net/fuxuemingzhu/article/details/83068632
# Python3 不可以直接将node存入heap, python2可以
class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = p = ListNode(0)
        heap = []
        heapq.heapify(heap)
        [heapq.heappush(heap, (l.val, i)) for i,l in enumerate(lists) if l]

        while heap:
            val, idx = heapq.heappop(heap)
            curHead = lists[idx]
            curNext = curHead.next
            p.next = curHead
            p = curHead
            if curNext:
                lists[idx] = curNext
                heapq.heappush(heap, (curNext.val, idx))
        
        return head.next