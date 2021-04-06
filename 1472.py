# 1472. Design Browser History
# Design

# runtime: faster than 94.87%
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        if len(self.history) > self.current:
            del self.history[self.current+1:]
        self.history.append(url)
        self.current += 1   

    def back(self, steps: int) -> str:
        if steps >= self.current:
            self.current = 0
            return self.history[0]
        else:
            self.current = self.current - steps
            return self.history[self.current]

    def forward(self, steps: int) -> str:
        if steps < len(self.history) - self.current - 1:
            self.current += steps
            return self.history[self.current]
        else:
            self.current = len(self.history) - 1
            return self.history[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)