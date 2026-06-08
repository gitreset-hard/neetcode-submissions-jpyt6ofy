from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minHeap = []
        for val, freq in count.items():
            heapq.heappush(minHeap, (freq, val))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [val for freq,val in minHeap]