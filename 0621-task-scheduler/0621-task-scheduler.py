class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # get count of tasks
        count = Counter(tasks)
        
        # maintain heap to keep track of highest frequency tasks
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        # create queue of tasks to process; [-count, idle_time]
        queue = deque()
        
        # while there are items in the queue, process most frequent task
        time = 0
        while queue or heap:
            time += 1
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time