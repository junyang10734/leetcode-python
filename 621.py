# Task Scheduler

# https://blog.csdn.net/fuxuemingzhu/article/details/81947087
# run time: faster than 96.45%
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        most = count.most_common()[0][1]
        num_most = len([i for i, v in count.items() if v == most])  # the number of ths most letter. eg.['A','A','A',B','B','B', C']  the counts of A and B are 3, then num_cost = 2 
        time = (most-1)*(n+1) + num_most
        return max(time, len(tasks))
  