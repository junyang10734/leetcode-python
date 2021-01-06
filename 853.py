# 853. Car Fleet
# Array

# https://leetcode.com/problems/car-fleet/solution/
# Sort
# running time: faster than 24.10%
class Solution1:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        print(cars)
        times = [(target-p)/s for p,s in cars]
        ans = 0
        
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]:
                ans += 1
            else:
                times[-1] = lead
            
        return ans + bool(times)


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