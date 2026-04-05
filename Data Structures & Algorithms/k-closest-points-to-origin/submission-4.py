from heapq import heapify, heappop, heappush
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        """
            sqrt(x**x + y**y) = dist

        """
        dist = [] # [[dist, coord]] = [[2, [0,2]], ...]
        heapify(dist)
        for x,y in points:
            distance = -(x**2 + y**2)
            heappush(dist, [distance, [x,y]])
            if len(dist) > k:
                heappop(dist)
        
        return [coord for dist, coord in dist]