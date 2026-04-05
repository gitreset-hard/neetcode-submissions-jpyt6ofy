from collections import Counter, deque
from heapq import heapify, heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        tasks = Counter(tasks)
        # valid tasks only
        tasks = [ -count for count in tasks.values()] #max heap
        heapify(tasks)
        cooldown = deque() # -cnt, idlTime
        time = 0 # total
        
        while tasks or cooldown:
            time += 1
            
            if tasks:
                count = heappop(tasks) + 1
                
                if count !=0:
                    cooldown.append([count, time +n])

            # check if cooldown is ready     
            if cooldown and cooldown[0][1] == time:
                heappush(tasks, cooldown.popleft()[0])
        
        return time
                
            


            

