from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if len(times) == 0: return 0

        graph = defaultdict(list)
        for src,dst, time in times:
            graph[src].append([dst,time])        

        best_times = {node: float('inf') for node in range(1,n+1)}
        best_times[k] = 0

        # ( best_time, node)
        minHeap = []
        heapq.heappush(minHeap, (0,k))
        while minHeap:
            
            curr_time, curr_node = heapq.heappop(minHeap)
            # already found a better way to get here
            print(curr_time, curr_node)
            if curr_time > best_times[curr_node]:
                print('*', curr_time, curr_node, best_times[curr_node])
                continue
            # how to prevent cycle check here? 
            for neighbor, travel_time in graph[curr_node]:
                next_time = curr_time + travel_time
                if next_time < best_times[neighbor]:
                    best_times[neighbor] = next_time
                    heapq.heappush(minHeap,(next_time, neighbor))
        
        time_taken = max(best_times.values())
        
        return time_taken if time_taken != float('inf') else -1



        
