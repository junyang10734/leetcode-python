# 382. Linked List Random Node
# Linked List
# 398

# https://blog.csdn.net/fuxuemingzhu/article/details/79488113
# running time: faster than 19.80%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.stack = []
        while head:
            self.stack.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return self.stack[random.randint(0, len(self.stack)-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()




# Reservoir sampling
# https://www.youtube.com/watch?v=A1iwzSew5Q
# https://leetcode.com/problems/linked-list-random-node/editorial/
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        scope = 1
        chosen_val = 0
        curr = self.head

        while curr:
            if random.random() < 1 / scope:
                chosen_val = curr.val
            curr = curr.next
            scope += 1
        
        return chosen_val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()