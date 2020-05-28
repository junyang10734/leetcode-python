# Decode String
# Stack

# https://blog.csdn.net/fuxuemingzhu/article/details/79332894
class Solution:
    def decodeString(self, s: str) -> str:
        curstring = ''
        stack = []
        curnum = 0
        
        for char in s:
            if char.isdigit():
                curnum = curnum * 10 + int(char)
            elif char == '[':
                stack.append(curstring)
                stack.append(curnum)
                curstring = ''
                curnum = 0
            elif char == ']':
                prenum = stack.pop()
                prestring = stack.pop()
                curstring = prestring + prenum * curstring
            else:
                curstring += char
            
        return curstring
