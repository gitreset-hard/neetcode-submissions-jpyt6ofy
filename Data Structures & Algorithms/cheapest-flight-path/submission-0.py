from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, cost in flights:
            graph[start].append((end,cost))

        prices = {city:float('inf') for city in range(n)}
        prices[src] = 0

        stops = 0
        q = deque()
        # (cost, city, stops)
        q.append((0, src, 0))
        while q:
            cost, city, stops = q.popleft()

            if stops > k:
                continue # why not break?

            for neighbor, price in graph[city]:
                new_cost = cost + price
                if new_cost < prices[neighbor]:
                    prices[neighbor] = new_cost
                    q.append((new_cost, neighbor, stops + 1))
            
        return prices[dst] if prices[dst] != float('inf') else -1


