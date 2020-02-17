# 动态规划
# n个台阶有两种到达方式：
# 从 n-1 台阶处 向上1次 1 step
# 从 n-2 台阶处 向上1次 2 
# runtime: O(n)  space: O(n)
class Solution1:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            res = [0] * (n+1)
            res[1] = 1
            res[2] = 2
            for i in range(n+1):
                if i > 2:
                    res[i] = res[i-1] + res[i-2]
            return res[n]


# runtime: O(n)  space: O(1)
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            first, second = 1, 2
            i = 3
            while(i<=n):
                steps = first + second
                first = second
                second = steps
                i = i + 1

            return steps