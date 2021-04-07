# 1244. Design A Leaderboard
# Design

# https://leetcode.com/problems/design-a-leaderboard/solution/

# Heap
# runtime: faster than 30.31%
class Leaderboard1:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
        else:
            self.scores[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for x in self.scores.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0



# Sorted Dictionary
# runtime: faster than 85.93%
from sortedcontainers import SortedDict
class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            preScore = self.scores[playerId]
            c = self.sortedScores[-preScore]
            if c == 1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] = c - 1
            
            newScore = preScore + score
            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1


    def top(self, K: int) -> int:
        count, total = 0, 0
        for k,v in self.sortedScores.items():
            if count + v <= K:
                total += (-k)*v
                count += v
                if count == K:
                    break
            else:
                t = K - count
                total += (-k)*t
                break
        return total

    def reset(self, playerId: int) -> None:
        score = self.scores[playerId]
        if self.sortedScores[-score] == 1:
            del self.sortedScores[-score]
        else:
            self.sortedScores[-score] -= 1
        del self.scores[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)