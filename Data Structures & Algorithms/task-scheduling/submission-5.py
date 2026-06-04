from collections import defaultdict, Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
            {X: 2,
             Y: 2}
        """
        tasks = Counter(tasks)
        heap = []
        for task, count in tasks.items():
            heapq.heappush(heap, (-count, task))
        
        cycles = 0
        # track remaining tasks: maxHeap b/c want to process the big tasks starting first so we can finish fast
        # (count, task)       
            
        # (next_free_time, count, task)
        cooldown = deque()

        while heap or cooldown:
            cycles += 1
            # can we process the cooldown?
            if cooldown and cooldown[0][0] <= cycles:
                _, count, task = cooldown.popleft()
                heapq.heappush(heap, (count, task))

            # biggest task, lets process it
            if heap:
                count, task = heapq.heappop(heap)
            count += 1 # add b/c it's stored as negative in heap
            if count < 0:
                cooldown.append((cycles+n + 1, count, task))

        return cycles



        
            