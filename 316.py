# 316. Remove Duplicate Letters
# Stack / String
# Same with 1081

# https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247486946&idx=1&sn=94804eb15be33428582544a1cd90da4d&chksm=9bd7f3eaaca07afc6fdfa94d05fa3007d9ecc54914a238e6deabeafd5032a299155505b40f2d&scene=21#wechat_redirect
# runtime: faster than 98.56%
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        inStack = {}
        cnt = collections.defaultdict(int)
        
        # 统计各字符字数
        for i in s:
            cnt[i] += 1
        
        # 重新遍历s, 字符数-1, 若该字符不在stack中，往前查看栈中元素是否大于该字符
        # 若栈中字符大于该字符，并且后面还有此栈中字符，则pop栈中字符
        for i in s:
            cnt[i] -= 1
            if i in inStack and inStack[i]:
                continue
            
            while stack and stack[-1] > i:
                if cnt[stack[-1]] == 0:
                    break
                inStack[stack.pop()] = False
                
            stack.append(i)
            inStack[i] = True
        
        res = ''
        for i in stack:
            res += i
        return res        