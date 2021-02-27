import collections;

def countLevelUpPlayers(cutOffRank, num, scores):
    if cutOffRank == 0:
        return 0
    
    cnt = collections.Counter(scores)
    scores = sorted(set(scores), reverse=True)

    res = 0
    for score in scores:
        if res >= cutOffRank:
            break
        res += cnt[score]

    return res


def countLevelUpPlayers(cutOffRank, num, scores):
    if cutOffRank == 0:
        return 0
    cnt = [0]*101
    for score in scores:
        cnt[score] += 1
    
    res = 0
    for i in range(100, 0, -1):
        if res >= cutOffRank:
            break
        else:
            res += cnt[i]

    return res

# cutOffRank = 3
# num = 4
# scores=[100, 50, 50, 25]
cutOffRank = 4
num = 5
scores=[2, 2, 3, 4, 5]
print(countLevelUpPlayers(cutOffRank, num, scores))