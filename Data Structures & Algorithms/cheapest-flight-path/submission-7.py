from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build graph. directed
        graph = defaultdict(list)
        
        for _from ,to, price in flights:
            graph[_from].append([to, price])

        # minHeap 
        # [cost, stops, city]
        minHeap = []
        minHeap.append([0,0,src])

        prices = [float('inf')]*n

        while minHeap:
            currCost, stops, city = heapq.heappop(minHeap)

            if city == dst:
                return currCost
                
            if stops > k:
                continue

            for nei, cost in graph[city]:
                nextCost = cost + currCost
                if nextCost > prices[nei]:
                    continue
                heapq.heappush(minHeap, [nextCost, stops + 1, nei])

        return prices[dst] if prices[dst]!=float('inf') else -1
                

