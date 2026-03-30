import heapq
from math import sqrt, floor
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        gifts = [-g for g in gifts]

        heapq.heapify(gifts)
        for _ in range(k):
            chosen = floor(sqrt(-heapq.heappop(gifts)))
            heapq.heappush(gifts, -chosen)
        
        return -sum(gifts)