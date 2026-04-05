from heapq import heapify, heappop, heappush
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        """
            sqrt(x**x + y**y) = dist

        """
        dist = [] # [[dist, coord]] = [[2, [0,2]], ...]

        for x,y in points:
            dist.append( [-(x**2 + y**2), [x,y]] )
        
        heapify(dist)

        while len(dist) > k:
            heappop(dist)
        
        return [coord for dist, coord in dist]