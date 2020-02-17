# Single Number
# sulotion2, sulotion3 and sulotion4 cost O(n) run time
# sulotion1 costs O(n*n) run time

# use one extra list, run slow
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        l = []
        for i in nums:
            if i in l:
                l.remove(i)
            else:
                l.append(i)
        
        return l[0]


# use one extra dictionary, run faster than solution1
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic.pop(i)
            else:
                dic[i] = 1
        
        return dic.popitem()[0]


# Math
# concept: 2∗(a+b+c)−(a+a+b+b+c)=c
class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)


# XOR
# If we take XOR of zero and some bit, it will return that bit
# a⊕0=a
# If we take XOR of two same bits, it will return 0
# a⊕a=0
# a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
# So we can XOR all bits together to find the unique number.
class Solution4:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a