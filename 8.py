# String to Integer (atoi)
# String

# https://blog.csdn.net/coder_orz/article/details/52053932
# runtime: faster than 97.65% 
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
            
        number, flag = 0, 1
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+':
            str = str[1:]
        
        for s in str:
            if s >= '0' and s <= '9':
                number = 10*number + ord(s) - ord('0')
            else:
                break
        
        number = flag * number
        number = number if number <= 2147483647 else 2147483647
        number = number if number >= -2147483648 else -2147483648
        
        return number