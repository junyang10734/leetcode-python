# Valid Palindrome
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for i in range(len(s)):
            if s[i].isalpha():
                l.append(s[i].lower())
            elif s[i].isnumeric():
                l.append(s[i])

        return l == l[::-1]


# more clear and more efficient
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        x = ''.join(i for i in s if i.isalpha() or i.isdigit())
        return x.lower() == x[::-1].lower()