# 1296. Divide Array in Sets of K Consecutive Numbers
# Same as 846

# https://blog.csdn.net/fuxuemingzhu/article/details/82530857
# running time: faster than 73.73%
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        cnt = collections.Counter(nums)
        
        for i in sorted(cnt):
            if cnt[i] > 0:
                for j in range(k)[::-1]:
                    if i+j not in cnt:
                        return False
                    cnt[i+j] -= cnt[i]
                    if cnt[i+j] < 0:
                        return False
        return True