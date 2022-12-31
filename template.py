# Sorting
# 92题 各种排序法

# Union-Find
class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]
        self.count = n
    
    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, p, q):
        rootp, rootq = self.find(p), self.find(q)
        if rootp == rootq:
            return
        if self.size[rootp] >= self.size[rootq]:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        else:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        self.count -= 1
    
    def getCount(self):
        return self.count



# slide window
def slidingWindow(s):
    window = {}
    left, right = 0, 0
    while right < len(s):
        # c 是将移入窗口的字符
        s = s[right]
        # 增大窗口
        right += 1
        # 进行窗口内数据更新
        # ...

        # 判断左侧窗口是否要收缩
        while window needs shrink:
            # d 是将移出窗口的字符
            d = s[left]
            # 缩小窗口
            left += 1
            # 进行窗口内数据更新
            # ...



# binary search
def binarySearch(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if mid == target:
            return mid
        elif mid < target:
            left = mid + 1
        elif mid > target:
            right = mid - 1
    return -1


# binary search left bound
def left_bound(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] == target:
            right = mid - 1
    
    if left == len(arr):
        return -1
    return left if arr[left] == target else -1


# binary search right bound
def right_bound(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] == target:
            left = mid + 1
    
    if left < 1:
        return -1
    return left - 1 if arr[left-1] == target else -1


# 单调栈
def nextGreaterElement(nums):
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        res[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    return res


# 计算器
class Solution:
    def calculate(self, s: str) -> int:
        def helper(s):
            stack = []
            sign = '+'
            num = 0
            
            while len(s) > 0:
                c = s.popleft()
                if c.isdigit():
                    num = num * 10 + int(c)
                if c == '(':
                    num = helper(s)
                         
                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] *= num
                    elif sign == '/':
                        stack[-1] = int(stack[-1] / float(num))
                    num = 0
                    sign = c
                
                if c == ')':
                    break
            
            return sum(stack)
                
        
        return helper(collections.deque(s))



# 前序遍历二叉树
def preOrderTraverse(root):
    if not root:
        return

    res = []
    res.append(root.val)
    res.addAll(preOrderTraverse(root.left))
    res.addAll(preOrderTraverse(root.right))
    return res


# 层级遍历
def levelTraverse(root):
    if not root:
        return
    
    queue = collections.deque([])
    queue.append(root)

    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return res


# 回溯 backtrack
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择


# backtrack 排列/组合/子集问题
# 1. 元素无重不可复选
# 组合/子集
def backtrack(nums: List[int], start: int):
    # 回溯算法标准框架
    for i in range(start, len(nums)):
        # 做选择
        track.append(nums[i])
        # 注意参数
        backtrack(nums, i + 1)
        # 撤销选择
        track.pop()

# 排列
def backtrack(nums: List[int]):
    for i in range(0, len(nums)):
        # 剪枝逻辑
        if used[i]:
            continue

        # 做选择
        used[i] = True
        track.append(nums[i])
        # 注意参数
        backtrack(nums)
        # 撤销选择
        used[i] = False
        track.pop()


# 2. 元素可重不可复选
# 组合/子集
nums.sort()
def backtrack(nums: List[int], start: int):
    # 回溯算法标准框架
    for i in range(start, len(nums)):
        # 剪枝逻辑，跳过值相同的相邻树枝
        if i > start and nums[i] == nums[i-1]:
            continue

        # 做选择
        track.append(nums[i])
        # 注意参数
        backtrack(nums, i + 1)
        # 撤销选择
        track.pop()

# 排列
nums.sort()
def backtrack(nums: List[int]):
    for i in range(0, len(nums)):
        # 剪枝逻辑
        if used[i]:
            continue
        # 剪枝逻辑，固定相同的元素在排列中的相对位置
        if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
            continue

        # 做选择
        used[i] = True
        track.append(nums[i])
        # 注意参数
        backtrack(nums)
        # 撤销选择
        used[i] = False
        track.pop()


# 3. 元素无重可复选
# 组合/子集
def backtrack(nums: List[int], start: int):
    # 回溯算法标准框架
    for i in range(start, len(nums)):
        # 做选择
        track.append(nums[i])
        # 注意参数
        backtrack(nums, i)
        # 撤销选择
        track.pop()

# 排列
def backtrack(nums: List[int]):
    # 回溯算法标准框架
    for i in range(len(nums)):
        # 做选择
        track.append(nums[i])
        # 注意参数
        backtrack(nums)
        # 撤销选择
        track.pop()


# BFS
# 计算从起点 start 到终点 target 的最近距离
def BFS(start: Node, target: Node):
    queue = collections.deque()
    visited = set()

    queue.append(start)
    visited.add(start)
    step = 0

    while queue:
        size = len(queue)
        for i in range(size):
            cur = queue.popleft()
            if cur is target:
                return step
            for nx in cur.adj():
                if nx not in visited:
                    queue.append(nx)
                    visited.add(nx)
        step += 1



# DP
# 自顶向下递归的动态规划
def dp(状态1, 状态2, ...):
    for 选择 in 所有可能的选择:
        # 此时的状态已经因为做了选择而改变
        result = 求最值(result, dp(状态1, 状态2, ...))
    return result

# 自底向上迭代的动态规划
# 初始化 base case
dp[0][0][...] = base case
# 进行状态转移
for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 求最值(选择1，选择2...)
