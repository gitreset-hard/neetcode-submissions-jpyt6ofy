from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = [(freq, val) for val, freq in count.items()]
        heapq.heapify(count)
        while len(count) > k:
            heapq.heappop(count)

        res = []
        for freq, element in count:
            res.append(element)
        return res