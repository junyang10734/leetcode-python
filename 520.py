# 520. Detect Capital
# String / Reg


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        n = len(word)
        if word[0].isupper() and word[1].isupper():
            for i in range(2, n):
                if word[i].islower():
                    return False
        else:
            for i in range(1, n):
                if word[i].isupper():
                    return False
        
        return True


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)