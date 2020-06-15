# Contains Duplicate III
# Array

# https://blog.csdn.net/qq_20141867/article/details/82024222
# runtime: faster than 22.16% 
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0:
            return False
        
        dic = collections.OrderedDict()
        for n in nums:
            key = n if not t else n // t
            print(key)
            for m in (dic.get(key-1), dic.get(key), dic.get(key+1)):
                print(m)
                if m is not None and abs(n-m) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = n
        
        return False