# Design Circular Queue
# design

# running time: faster than 90.33%
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.size = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue.append(value)
            self.rear += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front += 1
            return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]      

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear-1]  

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return self.rear - self.front == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()