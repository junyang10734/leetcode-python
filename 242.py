# Valid Anagram

# brute: faster than 5.15% 
class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = s.count(s[i])
                
        for i in range(len(t)):
            if t[i] not in d or d[t[i]] != t.count(t[i]):
                return False

        return True


# sort: faster than 72.83%
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s = list(str(s))
        t = list(str(t))
        if sorted(s) == sorted(t):
            return True
        else:
            return False


# run time: O(n)
# faster than 30.60%
class Solution3(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        l = [0] * 26
        for i in range(len(s)):
            l[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            l[ord(t[i]) - ord('a')] -= 1
            if l[ord(t[i]) - ord('a')] < 0:
                return False
        return True


# same as solution3, change list to dictionary
# dictionary is faster than list
# faster than 59.82%
class Solution4(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        l = {}
        for i in range(len(s)):
            if s[i] not in l:
                l[s[i]] = 1
            else:
                l[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in l:
                return False
            else:
                l[t[i]] -= 1
                if l[t[i]] < 0:
                    return False

        return True