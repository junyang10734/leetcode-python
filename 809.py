# 809. Expressive Words
# string

# https://blog.csdn.net/fuxuemingzhu/article/details/80678582
# running time: faster than 30.70%
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        if not S:
            return 0
        res = 0
        S_set = set(S)
        S_list = []
        pre_s, pre_index = S[0], 0
        
        for i, s in enumerate(S):
            if pre_s != s:
                S_list.append(S[pre_index:i])
                pre_s, pre_index = s, i
            if i == len(S) - 1:
                S_list.append(S[pre_index:])
        
           
        for word in words:
            if set(word) != S_set:
                continue
            
            word_list = []
            pre_w, pre_index = word[0], 0
            for i, w in enumerate(word):
                if pre_w != w:
                    word_list.append(word[pre_index:i])
                    pre_w, pre_index = w, i
                if i == len(word) - 1:
                    word_list.append(word[pre_index:])
            
            if len(word_list) == len(S_list):
                if all(S_list[i] == word_list[i] if len(S_list[i]) < 3 else len(S_list[i]) >= len(word_list[i]) for i in range(len(S_list))):
                    res += 1
        
        return res