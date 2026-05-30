import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for x,y,t in times:
            graph[x].append((y,t))

        times = {node: float('inf') for node in range(1,n+1)}
        times[k] = 0

        minHeap = [(0,k)]
        while minHeap:
            cur_time, cur_node = heapq.heappop(minHeap)
            
            if cur_time > times[cur_node]: 
                continue

            for neighbor, time in graph[cur_node]:
                _time = time + cur_time
                if _time < times[neighbor]:
                    times[neighbor] = _time
                    heapq.heappush(minHeap, (_time, neighbor))
            
        time_taken = max(times.values())
        return time_taken if time_taken != float('inf') else -1

                