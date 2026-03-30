import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            s1,s2 = heapq.heappop(stones), heapq.heappop(stones)
            diff = abs(s1 - s2)
            if diff > 0:
                heapq.heappush(stones, -diff)
            
        return -stones[0] if stones else 0
