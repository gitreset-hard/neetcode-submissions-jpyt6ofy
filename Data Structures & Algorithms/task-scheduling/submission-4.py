from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        time = 0
        cooldown  = deque()
        tasks = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(tasks)
        while tasks or cooldown:
            time += 1

            if cooldown and cooldown[0][1] <= time:
                cnt, _ = cooldown.popleft()
                heapq.heappush(tasks, cnt)
            
            if tasks:
                task = heapq.heappop(tasks) + 1
                # processed
                # now push to cooldown
                if task < 0:
                    cooldown.append((task, time + n + 1))
        
        return time

