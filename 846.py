# 846. Hand of Straights
# Same as 1296

# Array / Ordered Map

# running time: faster than 23.49%
class Solution1:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        cnt = collections.Counter(hand)
        
        while cnt:
            m = min(cnt)
            for k in range(m, m+W):
                v = cnt[k]
                if not v:
                    return False
                if v == 1:
                    del cnt[k]
                else:
                    cnt[k] -= 1
            
        return True


# https://blog.csdn.net/fuxuemingzhu/article/details/82530857
# Same as solution1, but with sorting
# running time: faster than 98.19%
class Solution2:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        cnt = collections.Counter(hand)
        for i in sorted(cnt):
            if cnt[i] > 0:
                for j in range(W)[::-1]:
                    if i + j not in cnt:
                        return False
                    cnt[i+j] -= cnt[i]
                    if cnt[i+j] < 0:
                        return False
        return True