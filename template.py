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
