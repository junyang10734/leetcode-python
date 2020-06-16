# Validate IP Address
# String

# https://blog.csdn.net/fuxuemingzhu/article/details/80682716
# runtime: faster than 69.38%
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP and self.checkIPv4(IP):
            return 'IPv4'
        elif ':' in IP and self.checkIPv6(IP):
            return 'IPv6'
        else:
            return 'Neither'
        
    def checkIPv4(self, IP):
        l = IP.split('.')
        if len(l) != 4:
            return False
        for i in l:
            if not i or (not i.isdecimal()) or (i[0] == '0' and len(i) != 1) or int(i) > 255:
                return False
        return True
        
    def checkIPv6(self, IP):
        IP = IP.lower()
        valid6 = '0123456789abcdef'
        if '::' in IP:
            return False
        l = IP.split(':')
        if len(l) > 8:
            return False
        for i in l:
            if not i: continue
            if len(i) > 4:
                return False
            for s in i:
                if s not in valid6:
                    return False
        return True
