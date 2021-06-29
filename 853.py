# 853. Car Fleet
# Array

# Sort
# runtime: O(nlogn)
class Solution1:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        arr = sorted(zip(position, speed), key=lambda x: x[0])
        prev = -1
        while arr:
            p, s = arr.pop()
            time = (target - p) / s
            if time <= prev:
                continue
            else:
                prev = time
                res += 1

        return res       


# https://blog.csdn.net/fuxuemingzhu/article/details/81867361
# Reverse Sort
# running time: faster than 72.52%
class Solution2:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0:
            return 0
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target-p)/s for p,s in cars]
        stack = [times[0]]
        
        for i in range(1,len(times)):
            if times[i] > stack[-1]:
                stack.append(times[i])
        
        return len(stack)