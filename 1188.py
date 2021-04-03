# 1188. Design Bounded Blocking Queue
# Concurrency

# https://leetcode.com/problems/design-bounded-blocking-queue/discuss/380191/Python3-Semaphore-Solution
# runtime: faster than 32.80%
import threading
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.queue.append(element)
        self.pulling.release()

    def dequeue(self) -> int:
        self.pulling.acquire()
        res = self.queue.popleft()
        self.pushing.release()
        return res

    def size(self) -> int:
        return len(self.queue)
