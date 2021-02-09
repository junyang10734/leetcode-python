# 707. Design Linked List
# Linked List / Design

# https://blog.csdn.net/danspace1/article/details/88948719
# runtime: faster than 50.08%
class Node():
    
    def __init__(self, val):
        self.val = val
        self.next = None
    
    
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size or self.head == None:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        cur = self.head
        if not cur:
            self.head = node
        else:
            while cur.next:
                cur = cur.next
            cur.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return 
        
        if index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            node = Node(val)
            node.next = cur.next
            cur.next = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        cur = self.head
        if index == 0:
            self.head = cur.next
        else:
            for i in range(index-1):
                cur = cur.next
            cur.next = cur.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)