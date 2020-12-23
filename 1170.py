# 1170. Compare Strings by Frequency of the Smallest Character
# hash / binary search

# https://blog.csdn.net/fuxuemingzhu/article/details/100179198
# hash
# running time: faster than 84.17%
class Solution1:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        d = {}
        for i in range(11):
            d[i] = 0
        
        for w in words:
            i = w.count(min(w))
            d[i] += 1
        
        
        res = []
        for q in queries:
            n = q.count(min(q))
            num = 0
            for i in range(10, n, -1):
                num += d[i]
            res.append(num)
        
        return res


# https://blog.csdn.net/CSerwangjun/article/details/102559817
# binary search
# running time: faster than 75.24%
class Solution2:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def biSearch(arr, target):
            l, r = 0, len(arr)-1
            while l <= r:
                mid = (l+r)//2
                if target >= arr[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        
        arr1 = [w.count(min(w)) for w in words]
        arr1.sort()

        arr2 = [q.count(min(q)) for q in queries]

        n = len(words)
        res = []
        for a in arr2:
            res.append(n-biSearch(arr1, a))
        
        return res