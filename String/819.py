# Most Common Word

# hash
# runtime: faster than 99.91% 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, ' ')
            
        str_list = paragraph.split(' ')
        str_dict = {}
        ban_dict = {}
        for i in banned:
            ban_dict[i] = 1

        for i in str_list:
            i = i.lower()
            if i != '':
                if i not in ban_dict:
                    if i not in str_dict:
                        str_dict[i] = 1
                    else:
                        str_dict[i] += 1

        com_word = ''
        num = 0
        for i in str_dict:
            if str_dict[i] > num:
                com_word = i
                num = str_dict[i]
        
        return com_word