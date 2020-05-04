# Last Stone Weight
# Stack / Greedy

# runtime: faster than 75.44%
class Solution1:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            m1 = max(stones)
            stones.remove(m1)
            m2 = max(stones)
            stones.remove(m2)

            if m1 != m2:
                stones.append(m1-m2)

        if len(stones) <= 0:
            return 0
        elif len(stones) == 1:
            return stones[0]


# runtime: faster than 99.76%
class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            m1 = stones[-1]
            m2 = stones[-2]
            stones.pop()
            stones.pop()
            
            if m1 > m2:
                stones.append(m1-m2)
        
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
