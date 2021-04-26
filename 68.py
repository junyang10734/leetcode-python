# 68. Text Justification
# String

# https://leetcode.com/problems/text-justification/discuss/24891/Concise-python-solution-10-lines.
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur = []
        num_of_letters = 0
        for w in words:
            if len(w) + len(cur) + num_of_letters > maxWidth:
                if len(cur) == 1:
                    res.append(cur[0] + ' '*(maxWidth - num_of_letters))
                else:
                    space_between_words, num_extra_space = divmod(maxWidth-num_of_letters, len(cur)-1)
                    for i in range(num_extra_space):
                        cur[i] += ' '
                    res.append((' '*space_between_words).join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        
        res.append(' '.join(cur) + ' '*(maxWidth - num_of_letters - len(cur) + 1))
        return res
