# 1348. Tweet Counts Per Frequency
# Design

# https://leetcode.com/problems/tweet-counts-per-frequency/discuss/503515/Python3-linear-scan
# runtime: O(n)
class TweetCounts:

    def __init__(self):
        self.tweets = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            seconds = 60
        elif freq == 'hour':
            seconds = 3600
        else:
            seconds = 86400
        
        res = [0] * ((endTime - startTime) // seconds + 1)
        for t in self.tweets[tweetName]:
            if startTime <= t <= endTime:
                res[(t - startTime) // seconds] += 1
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)