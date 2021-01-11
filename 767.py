# 767. Reorganize String

# https://blog.csdn.net/fuxuemingzhu/article/details/80680454

# Counter
# running time: faster than 6.09%
class Solution:
    def reorganizeString(self, S: str) -> str:
        cnt = collections.Counter(S)
        ans = '#'
        
        while cnt:
            stop = True
            for i,n in cnt.most_common():
                if ans[-1] != i:
                    ans += i
                    cnt[i] -= 1
                    if not cnt[i]:
                        del cnt[i]
                    stop = False
                    break
                    
            if stop:
                break
        
        return ans[1:] if len(ans) == len(S) + 1 else ''
