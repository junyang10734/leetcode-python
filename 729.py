# 729. My Calendar I

# Array / Tree
# https://leetcode.com/problems/my-calendar-i/solution/

# Array
# running time: faster than 27.90%
class MyCalendar1:

    def __init__(self):
        self.c = []

    def book(self, start: int, end: int) -> bool:
        for s,e in self.c:
            if s < end and start < e:
                return False
        self.c.append((start,end))
        return True


# BTS 
# running time: faster than 66.62%
class Node:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left, self.right = None, None
    
    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False
            
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(Node(start, end))
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)