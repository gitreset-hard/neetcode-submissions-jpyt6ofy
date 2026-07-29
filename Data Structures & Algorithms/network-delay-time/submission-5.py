import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
       
        graph = defaultdict(list)
        for src, dst, wt in times:
            graph[src].append([dst, wt])
        
        heap = []
        heap.append([0,k]) # time, node
        seen = set() # djikstras visits the each node optimally the first time

        while heap:
            wt, curr = heapq.heappop(heap)
            if curr in seen:
                continue
            seen.add(curr)

            if len(seen) == n:
                return wt
            
            for nei, wt_nei in graph[curr]:
                if nei not in seen:
                    heapq.heappush(heap, [wt_nei + wt, nei])
                    

        return -1
