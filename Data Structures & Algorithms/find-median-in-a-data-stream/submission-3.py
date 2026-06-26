import heapq
class MedianFinder:
    """ 
    brainstorm
    - if using simple list, then adding & sorting new num is O(logN)
    - does storing min/max help? no i don't think so
        - storing length could
    - make two heaps? 1 for smaller and 1 for larger if split in half?

    """
    def __init__(self):
        self.smaller = [] # maxHeap: keep largest of small at top
        self.larger = [] # minHeap: smallest of large at top

    def addNum(self, num: int) -> None:
        # they will either be equal lenght or differ by 1
        # i don't think which matters
        """
            small:  1
            large: 
        """
        # push to smaller and then push the largest to large. 
        heapq.heappush(self.smaller, -num)
        val = heapq.heappop(self.smaller)
        heapq.heappush(self.larger, -val)
        
        # balance
        # -1 -2  : 6 7 8 9 
        if len(self.smaller) < len(self.larger):
            val = heapq.heappop(self.larger)
            heapq.heappush(self.smaller, -val)
       
    def findMedian(self) -> float:
        # even : -1 -2 -3 vs 4 5 6
        if len(self.smaller) == len(self.larger):
            return (-self.smaller[0] + self.larger[0]) / 2
        # -1 -2 -3 -4 vs 5 6 7
        else:
            return -self.smaller[0] / 1.0
