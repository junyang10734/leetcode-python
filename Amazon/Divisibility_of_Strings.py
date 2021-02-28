def divisibility(s, t):
    def repeater(s0):
        i = (s0+s0)[1:-1].find(s0)
        if i == -1:
            return s0
        else:
            return s0[:i+1]

    slen, tlen = len(s), len(t)
    tcopy = t
    while(slen > tlen):
        t = tcopy + t
        tlen = len(t)
    if(s == t):
        rt = repeater(t)
        return len(rt)
    else:
        return -1


s = "gcdgcdgcdgcdgcdgcd"
t = "gcdgcd"
print(divisibility(s, t))