# 1834. Single-Threaded CPU
# heap

# https://leetcode.com/problems/single-threaded-cpu/solutions/2216661/single-threaded-cpu/
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_processing_order = []
        sorted_tasks = [(enqueue, process, idx) for idx, (enqueue, process) in enumerate(tasks)]
        sorted_tasks.sort()
        next_tasks = []
        curr_time = 0
        task_index = 0

        while task_index < len(tasks) or next_tasks:
            if not next_tasks and curr_time < sorted_tasks[task_index][0]:
                curr_time = sorted_tasks[task_index][0]
            
            while task_index < len(sorted_tasks) and curr_time >= sorted_tasks[task_index][0]:
                enqueue_time, process_time, original_index = sorted_tasks[task_index]
                heapq.heappush(next_tasks, (process_time, original_index))
                task_index += 1
            
            process_time, index = heapq.heappop(next_tasks)
            curr_time += process_time
            tasks_processing_order.append(index)
        
        return tasks_processing_order