# Count of Smaller Numbers After Self

# http://bookshadow.com/weblog/2015/12/06/leetcode-count-of-smaller-numbers-after-self/
# https://zxi.mytechroad.com/blog/algorithms/array/leetcode-315-count-of-smaller-numbers-after-self/


# FenwickTree / Binary Indexed Tree
# faster than 55.91%
class Solution1:
    def countSmaller(self, nums: List[int]) -> List[int]:
        idx = {}
        for k,v in enumerate(sorted(set(nums))):
            idx[v] = k + 1
        
        inums = [idx[x] for x in nums]
        ft = FenwickTree(len(inums))
        ans = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ft.sum(inums[i]-1)
            ft.add(inums[i], 1)
        return ans        

        
class FenwickTree(object):
    def __init__(self, n):
        self.n = n
        self.sums = [0] * (n+1)
        
    def add(self, x, val):
        while x <= self.n:
            self.sums[x] += val
            x += self.lowbit(x)
    
    def lowbit(self, x):
        return x & -x
    
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sums[x]
            x -= self.lowbit(x)
        return res



# BST
# faster than 66.96%
class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        bst = BinarySearchTree()
        for i in range(len(nums)-1, -1, -1):
            ans[i] = bst.insert(nums[i])
        return ans
        
        
class TreeNode(object):
    def __init__(self, val):
        self.leftCnt = 0
        self.val = val
        self.cnt = 1
        self.left = None
        self.right = None
        
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return 0
        root = self.root
        cnt = 0
        while root:
            if val < root.val:
                root.leftCnt += 1
                if root.left is None:
                    root.left = TreeNode(val)
                    break
                root = root.left
            elif val > root.val:
                cnt += root.leftCnt + root.cnt
                if root.right is None:
                    root.right = TreeNode(val)
                    break
                root = root.right
            else:
                cnt += root.leftCnt
                root.cnt += 1
                break
        return cnt
        

# merge sort
# official solution
# Time Limit Exceeded
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [[v, i] for i,v in enumerate(nums)]
        res = [0] * n

        def sort(arr, left, right):
            if right - left <= 1:
                return
            
            mid = (left + right) // 2
            sort(arr, left, mid)
            sort(arr, mid, right)
            merge(arr, left, right, mid)

        def merge(arr, left, right, mid):
            i, j = left, mid
            temp = []
            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    res[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            
            while i < mid:
                res[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1

            while j < right:
                temp.append(arr[j])
                j += 1
            
            for i in range(left, right):
                arr[i] = temp[i - left]

        sort(arr, 0, n)
        return res
