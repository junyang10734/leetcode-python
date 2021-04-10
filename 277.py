# 277. Find the Celebrity
# Array

# TLE
class Solution1:
    def findCelebrity(self, n: int) -> int:
        self.knowOthers = collections.defaultdict(int)
        self.otherKnows = collections.defaultdict(int)
        notC = set()
        
        for i in range(n-1):
            for j in range(i+1, n):
                if knows(i, j):
                    self.knowOthers[i] += 1
                    self.otherKnows[j] += 1
                    notC.add(i)
                if knows(j, i):
                    self.knowOthers[j] += 1
                    self.otherKnows[i] += 1
                    notC.add(j)
        
        if len(notC) == n:
            return -1
        
        for i in range(n):
            if i not in notC:
                if self.knowOthers.get(i, 0) == 0 and self.otherKnows[i] == n-1:
                    return i
        return -1


# https://leetcode.com/problems/find-the-celebrity/solution/
# runtime: O(n)
class Solution2:
    def findCelebrity(self, n: int) -> int:
        c = 0
        for i in range(1, n):
            if knows(c, i):
                c = i
        
        for j in range(n):
            if j == c:
                continue
            if knows(c, j) or not knows(j, c):
                return -1
        
        return c