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


def cut_off_rank(cut_off: int, scores: List[int]) -> int:
    counts = collections.Counter(scores)

    lvlups = 0
    score = 100
    while score > 0 and lvlups < cut_off:
        lvlups += counts[score]
        score -= 1
    # now either lvlups >= cut_off (have enough players at least cut_off rank),
    # or score = 0 (every non-zero player levels up)
    return lvlups


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