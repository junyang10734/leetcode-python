# 716. Max Stack
# Stack

# runtime: faster than 74.75%
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        mx = max(self.stack)
        i = len(self.stack) - 1
        while i >= 0:
            if self.stack[i] == mx:
                break
            i -= 1
        self.stack = self.stack[:i] + self.stack[i+1:]
        return mx
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()