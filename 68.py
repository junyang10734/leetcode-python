# 68. Text Justification
# String

# runtime: faster than 58.10%
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        count = 0
        for word in words:
            if count + len(word) <= maxWidth:
                line.append(word)
                count += len(word) + 1
            else:
                n = len(line)
                blanks_count = maxWidth - count + n
                new_line = []
                i = 0
                while i < n:
                    new_line.append(line[i])
                    if i < n-1:
                        blanks = ceil(blanks_count/(n-i-1))
                        new_line.append(' '*blanks)
                        blanks_count -= blanks
                    i += 1
                this_line = ''.join(new_line)
                this_line += ' '*(maxWidth-len(this_line))
                res.append(this_line)
                line = [word]
                count = len(word)+1
        
        last_line = ' '.join(line)
        last_line += ' '*(maxWidth-len(last_line))
        res.append(last_line)
        return res