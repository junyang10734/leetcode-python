# Different Ways to Add Parentheses
# DaC and Recursive

# https://blog.csdn.net/fuxuemingzhu/article/details/79568487

# Recursive
# runtime: faster than 6.22%
class Solution1:
    def diffWaysToCompute(self, input: str) -> List[int]:
        d = {}
        nums, ops = [], []
        input = re.split(r'(\D)', input)
        for x in input:
            if x.isdigit():
                nums.append(x)
            else:
                ops.append(x)
        self.dfs(nums, ops, d)
        return d.values()

    def dfs(self, nums, ops, d):
        if ops:
            for x in range(len(ops)):
                self.dfs(nums[:x] + ['(' + nums[x] + ops[x] + nums[x + 1] + ')'] + nums[x + 2 :], ops[:x] + ops[x+1:], d)
        elif nums[0] not in d:
            d[nums[0]] = eval(nums[0])


# DaC
# runtime: faster than 80.15% 
class Solution2:
    def diffWaysToCompute(self, input: str) -> List[int]:
        res = []
        for i in range(len(input)):
            if input[i] == '+' or input[i] == '-' or input[i] == '*':
                lefts = self.diffWaysToCompute(input[:i])
                rights = self.diffWaysToCompute(input[i+1:])
                for l in lefts:
                    for r in rights:
                        if input[i] == '+':
                            res.append(l + r)
                        elif input[i] == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        
        if not res:
            res.append(int(input))
        return res
