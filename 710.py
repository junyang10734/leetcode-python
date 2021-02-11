# 710. Random Pick with Blacklist
# Design / Hash

# labuladong算法小抄
# https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247487414&idx=1&sn=2be87c0c9279da447f8ac8b8406230fe&chksm=9bd7f1beaca078a865357f58ba2ff12b46490b0a773c0221e0a846c67950fa9c661664ad500e&scene=21#wechat_redirect
# runtime: faster than 57.74%
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.size = N - len(blacklist)
        self.d = {}
        for b in blacklist:
            self.d[b] = 1
        
        last = N - 1
        for b in blacklist:
            if b >= self.size:
                continue
            while last in self.d:
                last -= 1
            self.d[b] = last
            last -= 1
        

    def pick(self) -> int:
        idx = random.randint(0, self.size-1)
        if idx in self.d:
            return self.d[idx]
        return idx



# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()