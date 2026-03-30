from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        """
        X X Y Y , n = 2
        !  
        next_time:
        x : 0 + n + 1 -> next at 3

        """

        maxHeap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1 # complete 1 task
                if cnt!= 0:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                cnt, _ = q.popleft()
                heapq.heappush(maxHeap, cnt)
        
        return time