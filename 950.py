# 950. Reveal Cards In Increasing Order
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/84728767
# running time: faster than 91.58%
class Solution1:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        que = collections.deque()
        for i in range(len(deck)):
            if que:
                que.appendleft(que.pop())
            que.appendleft(deck.pop())
        return list(que)


# https://leetcode.com/problems/reveal-cards-in-increasing-order/solution/
# running time: faster than 76.55% 
# Same idea with solution1. different methods
class Solution2:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        index = collections.deque(range(N))
        ans = [None]*N

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())
        
        return ans
 