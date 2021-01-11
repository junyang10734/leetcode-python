# 731. My Calendar II
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/82820204
# running time: faster than 9.98%
class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlapped = []

    def book(self, start: int, end: int) -> bool:
        for s,e in self.overlapped:
            if max(start, s) < min(end, e):
                return False
        
        for s,e in self.booked:
            ss = max(s, start)
            ee = min(e, end)
            if ss < ee:
                self.overlapped.append((ss,ee))
        self.booked.append((start, end))
        
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)


# https://leetcode.com/problems/my-calendar-ii/solution/
# running time: faster than 36.99%
# Same as above, modifies some expression
class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlapped = []

    def book(self, start: int, end: int) -> bool:
        for s,e in self.overlapped:
            if start < e and end > s:
                return False
        
        for s,e in self.booked:
            if start < e and end > s:
                self.overlapped.append((max(start, s), min(end, e)))
        self.booked.append((start, end))
        
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)