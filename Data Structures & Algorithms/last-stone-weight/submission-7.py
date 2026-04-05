import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        """
        2 heaviest stones: x, y
        x == y -> x=y = 0
        x < y -> c: y-x
        """

        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x , y = heapq.heappop(stones), heapq.heappop(stones)
            diff = abs(x-y)
            if diff > 0:
                heapq.heappush(stones, -diff)
            
        
        return -stones[0] if len(stones) > 0 else 0

        