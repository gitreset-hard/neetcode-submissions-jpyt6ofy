from collections import defaultdict, deque
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for start, end, cost in flights:
            graph[start].append((end, cost))
        
        minHeap = []
        # (cost, stops, city)
        # keeps lowest cost at top of heap so we know the first time we get to a dest is cheapest
        minHeap.append((0, 0, src))

        # need to track best price at each stop. the heap only tracks the current path it's on
        prices = {stop:float('inf') for stop in range(n)}
        prices[src] = 0

        q = deque([(0, 0, src)])
        while q:
            cost, stops, city = q.popleft()
            
            # can't stop here. if the  k + 1 stop is the dst, it's fine
            if stops > k:
                continue
            
            for neighbor, next_cost in graph[city]:
                cost_to_fly = cost + next_cost

                if cost_to_fly <= prices[neighbor]:
                    prices[neighbor] = cost_to_fly
                    q.append((cost_to_fly, stops + 1, neighbor))
    
        return prices[dst] if prices[dst] != float('inf') else -1
                

    
