# 849. Maximize Distance to Closest Person
# Array

# https://leetcode.com/problems/maximize-distance-to-closest-person/solution/

# Next Array
# running time: faster than 5.56% 
class Solution1:
    def maxDistToClosest(self, seats: List[int]) -> int:
        N = len(seats)
        left, right = [N] * N, [N] * N
        
        for i in range(N):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i-1] + 1
        
        for i in range(N-1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < N-1:
                right[i] = right[i+1] + 1
        
        return max(min(left[i],right[i]) for i,seat in enumerate(seats) if not seat)


# Two Pointer
# running time: faster than 5.56%
class Solution2:
    def maxDistToClosest(self, seats: List[int]) -> int:
        people = (i for i,seat in enumerate(seats) if seat)
        prev, future = None, next(people)
        res = 0
        
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)
                
                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                res = max(res, min(left, right))
        return res
                

# Group by Zero
# running time: faster than 5.56%
class Solution3:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = seats.index(1)
        seats.reverse()    
        res = max(res, seats.index(1))
        
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                res = max(res, (K+1)//2)
        return res
