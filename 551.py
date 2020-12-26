# 551. Student Attendance Record I
# string

# running time: faster than 50.27%
class Solution1:
    def checkRecord(self, s: str) -> bool:
        A, L = 0, 0
        l_flag = False
        for char in s:
            if char == "A":
                if A == 1:
                    return False
                else:
                    A += 1
                    L = 0
            elif char == "L":
                if L == 2:
                    return False
                else:
                    L += 1
            else:
                L = 0
        
        return True


# 正则表达式
# running time: faster than 79.75% 
class Solution2:
    def checkRecord(self, s: str) -> bool:
        return not re.match(".*A.*A.*", s) and not re.match(".*LLL.*", s)