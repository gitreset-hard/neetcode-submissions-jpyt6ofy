from math import inf
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        2 3 1 5 4                   1 2 3 4 5
        2 3
        4 5 

                        

        """
        heap = []
        heapq.heapify(heap)
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heapq.heappop(heap)
