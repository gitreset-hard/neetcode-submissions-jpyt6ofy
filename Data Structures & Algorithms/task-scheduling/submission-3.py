import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        tasks = Counter(tasks)
        maxHeap = [-val for val in tasks.values()]
        heapq.heapify(maxHeap)
        cooldown = [] # queue
        time = 0

        while maxHeap or cooldown:
            if cooldown and cooldown[0][1] <= time:
                heapq.heappush(maxHeap, cooldown.pop(0)[0])

            if maxHeap:
                curr = heapq.heappop(maxHeap)
                curr += 1

                if curr < 0:
                    cooldown.append((curr, time + n + 1))

            time += 1
        
        return time

