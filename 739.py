# Daily Temperatures
# 503
# Hash Table / Stack 单调递减栈

# https://blog.csdn.net/fuxuemingzhu/article/details/79285081
# Hash Table
# runtime: faster than 9.26%
class Solution1:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        nxt = {}
        res = []
        for day in range(len(T)-1, -1, -1):
            temp = T[day]
            nxt[temp] = day
            larger = []
            for i in range(temp+1, 101):
                if i in nxt:
                    larger.append(nxt[i] - day)
            if larger:
                res.append(min(larger))
            else:
                res.append(0)
        
        return res[::-1]


# https://blog.csdn.net/qq_17550379/article/details/86494645?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
# Stack 单调递减栈
# runtime: faster than 99.36%
class Solution2:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        
        for i,j in enumerate(T):
            while stack and T[stack[-1]] < j:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        
        return res


# 单调栈 - 模板
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return res