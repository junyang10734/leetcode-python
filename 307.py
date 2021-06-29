# 307. Range Sum Query - Mutable


# Segment Tree
# runtime: O(n)
# https://leetcode.com/problems/range-sum-query-mutable/discuss/75784/Python%3A-Well-commented-solution-using-Segment-Trees
class Node():
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
        self.total = 0

class NumArray:

    def __init__(self, nums: List[int]):
        
        def createTree(nums, l, r):
            if l > r:
                return
            elif l == r:
                node = Node(l, r)
                node.total = nums[l]
                return node
            else:
                mid = (l + r) // 2
                root = Node(l, r)
                root.left = createTree(nums, l, mid)
                root.right = createTree(nums, mid+1, r)
                root.total = root.left.total + root.right.total
                return root
        
        self.root = createTree(nums, 0, len(nums)-1)
        
        
    def update(self, index: int, val: int) -> None:
        
        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return val
            
            mid = (root.start + root.end) // 2
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            
            root.total = root.left.total + root.right.total
            return root.total
        
        updateVal(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        
        def getSum(root, i, j):
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            if j <= mid:
                return getSum(root.left, i, j)
            elif i >= mid + 1:
                return getSum(root.right, i, j)
            else:
                return getSum(root.left, i, mid) + getSum(root.right, mid+1, j)
        
        return getSum(self.root, left, right)



# Naive
# TLE
class NumArray1:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        for i in range(left, right+1):
            res += self.nums[i]
        return res



# https://www.cnblogs.com/grandyang/p/4985506.html
# divide array to some blocks
# running time: faster than 18.59%
class NumArray2:

    def __init__(self, nums: List[int]):
        self.nums = nums
        N = len(nums)
        root = sqrt(N)
        self.block = math.ceil(N / root)
        self.sums = [0] * self.block
        for i in range(N):
            self.sums[i//self.block] += nums[i]

    def update(self, index: int, val: int) -> None: 
        idx = index // self.block
        self.sums[idx] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        l, r = left // self.block, right // self.block
        
        if l == r:
            for i in range(left,right+1):
                total += self.nums[i]
            return total
        
        for i in range(left, (l+1)*self.block):
            total += self.nums[i]
            
        for j in range(r*self.block, right+1):
            total += self.nums[j]        

        for n in range(l+1, r):
            total += self.sums[n]
        
        return total



# http://bookshadow.com/weblog/2015/11/18/leetcode-range-sum-query-mutable/
# Segment Tree
# running time: faster than 19.92% 
class NumArray3:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.size = len(nums)
        h = int(math.ceil(math.log(self.size,2)))
        maxSize = 2 ** (h+1) - 1
        self.st = [0] * maxSize
        self.initST(0, self.size-1, 0)

    def update(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        diff = val - self.nums[index]
        self.nums[index] = val
        self.updateST(0, self.size-1, index, diff, 0)

    def sumRange(self, left: int, right: int) -> int:
        if left < 0 or right < 0 or left >= self.size or right >= self.size:
            return 0
        return self.getSumST(0, self.size-1, left, right, 0)
        
    def initST(self, ss, se, si):
        if ss == se:
            self.st[si] = self.nums[ss]
        else:
            mid = (ss+se) // 2
            self.st[si] = self.initST(ss,mid,si*2+1) + self.initST(mid+1, se, si*2+2)
            
        return self.st[si]
        
    def updateST(self, ss, se, index, diff, si):
        if index < ss or index > se:
            return
        self.st[si] += diff
        if ss != se:
            mid = (ss+se)//2
            self.updateST(ss, mid, index, diff, si*2+1)
            self.updateST(mid+1, se, index, diff, si*2+2)
        

    def getSumST(self, ss, se, qs, qe, si):
        if qs <= ss and qe >= se:
            return self.st[si]
        if se < qs or ss > qe:
            return 0
        mid = (ss+se)//2
        return self.getSumST(ss,mid,qs,qe,si*2+1) + self.getSumST(mid+1, se,qs,qe,si*2+2)



# https://www.hrwhisper.me/leetcode-range-sum-query-mutable/
# Binary Indexed Tree
# running time: faster than 22.64%
class NumArray4:

    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.sums = [0] * (self.size + 1)
        self.nums = nums
        for i in range(self.size):
            self.add(i+1, nums[i])

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.add(index+1, diff)
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(right+1) - self.getSum(left)
        
    def add(self, i, val):
        while i <= self.size:
            self.sums[i] += val
            i += self.lowbit(i)
            
    def lowbit(self, i):
        return i & -i
    
    def getSum(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= self.lowbit(i)
        return res



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)