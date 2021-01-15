# 855. Exam Room
# Compare with 849
# Array

# https://leetcode.com/problems/exam-room/solution/
# running time: faster than 39.43%
class ExamRoom:

    def __init__(self, N: int):
        self.size = N
        self.arr = []

    def seat(self) -> int:
        if not self.arr:
            res = 0
        else:
            d = self.arr[0]
            res = 0
            
            for i,s in enumerate(self.arr):
                if i:
                    prev = self.arr[i-1]
                    d0 = (s-prev)//2
                    if d0 > d:
                        d = d0
                        res = prev + d
            
            d1 = self.size - 1 - self.arr[-1]
            if d1 > d:
                res = self.size - 1
        
        bisect.insort(self.arr, res)
        return res

    def leave(self, p: int) -> None:
        self.arr.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)