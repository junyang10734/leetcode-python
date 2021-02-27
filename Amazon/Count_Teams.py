def teams(num, lengths, minReviews, minLength, maxLength):
    res = 0

    arr = []
    for n in lengths:
        if minLength <= n <= maxLength:
            arr.append(n)
    
    d = {}
    maxReviews = len(arr)
    if maxReviews == minReviews:
        return 1
    elif maxReviews < minReviews:
        return 0
    else:

        def getMul(n, t):
            mul = 1
            while t > 0:
                mul *= n
                n -= 1
                t -= 1
            return mul

        for i in range(minReviews, maxReviews+1):
            if i not in d:
                n = getMul(maxReviews, i) // getMul(i, i)
                d[maxReviews-i] = n
                res += n
            else:
                res += d[i]


    return res


print(teams(10, [6, 13, 5, 10, 12, 4, 2, 15, 7, 7], 3, 4, 10))