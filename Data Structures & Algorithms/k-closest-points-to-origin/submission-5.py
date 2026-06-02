import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        for pt in points:
            x,y = pt
            diff = x**2 + y**2
            heapq.heappush(minHeap, [-diff, pt])
            while len(minHeap) > k:
                heapq.heappop(minHeap)
            
        res = [pt for diff, pt in minHeap]
        return res
