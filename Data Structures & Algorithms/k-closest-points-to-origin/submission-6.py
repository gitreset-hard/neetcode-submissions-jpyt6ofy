import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for x,y in points:

            # dist to origin (0,0) --> x2 = 0
            # don't need sq root b/c comparing all the same
            # minHeap keeps smallest on top
            dist = x*x + y*y
            heapq.heappush(heap, [-dist, [x,y]])
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [pt for dist, pt in heap]
            